PORTNAME=	backuppc
DISTVERSION=	4.4.1.20231111
PORTREVISION=	1
CATEGORIES=	sysutils
PKGNAMESUFFIX=	-devel

MAINTAINER=	moiseev@mezonplus.ru
COMMENT=	Multi-platform backup to disk-based storage
WWW=		https://backuppc.github.io/backuppc/

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

EXTRACT_DEPENDS=	p5-BackupPC-XS>=0.62:sysutils/p5-BackupPC-XS
RUN_DEPENDS=	p5-CGI>0:www/p5-CGI \
		p5-File-Listing>=0:sysutils/p5-File-Listing \
		p5-BackupPC-XS>=0.62:sysutils/p5-BackupPC-XS

USES=		cpe perl5

.if defined(QEMU_EMULATING) && "${QEMU_EMULATING}" == "1"
BROKEN=		fails to build under qemu: uncaught target signal 11 (Segmetation fault) - core dumped
.endif

CONFLICTS_INSTALL=	backuppc backuppc4

CPE_VENDOR=	craig_barratt

USE_GITHUB=	yes
GH_TAGNAME=	174e707
USE_PERL5=	extract
NO_BUILD=	yes
NO_ARCH=	yes
USE_RC_SUBR=	backuppc

WRKSRC_SUBDIR=	dist/BackupPC-${PORTVERSION}

USERS=		backuppc
GROUPS=		backuppc

DOCSDIR=	${PREFIX}/share/doc/BackupPC
CGIDIR?=	${PREFIX}/www/cgi-bin

SUB_FILES=	pkg-deinstall pkg-message update.sh
SUB_LIST=	CGIDIR=${CGIDIR}

PLIST_SUB+=	CGIDIR=${CGIDIR:S,^${PREFIX}/,,} \
		DISTVERSION=${DISTVERSION}

PORTDOCS=	ChangeLog LICENSE README.md

OPTIONS_DEFINE=		ARCHIVE_ZIP DOCS RSYNC_BPC \
			RRDTOOL SMB XML_RSS

OPTIONS_DEFAULT=	ARCHIVE_ZIP

ARCHIVE_ZIP_DESC=	Install Perl module for Zip archive files
RSYNC_BPC_DESC=		Install modified rsync that used as part of BackupPC
RRDTOOL_DESC=		Install Round Robin Database Tools
SMB_DESC=		Install Samba (for "smb" transfer and NetBIOS lookup)
XML_RSS_DESC=		Install Perl extension to manage RSS files

ARCHIVE_ZIP_RUN_DEPENDS=	p5-Archive-Zip>=0:archivers/p5-Archive-Zip
RSYNC_BPC_RUN_DEPENDS=		rsync-bpc>=3.0.9.15:net/rsync-bpc
RRDTOOL_RUN_DEPENDS=		rrdtool:databases/rrdtool
SMB_USES=			samba:run # nmblookup, smbclient
XML_RSS_RUN_DEPENDS=		p5-XML-RSS>=0:textproc/p5-XML-RSS

post-extract:
	cd ${WRKDIR}/${PORTNAME}-${GH_TAGNAME} && ${PERL} makeDist \
		--nosyntaxCheck \
		--version ${PORTVERSION}

do-install:
	cd ${WRKSRC} && ${PERL} configure.pl	\
		--batch				\
		--backuppc-user ${USERS}	\
		--bin-path perl=${PERL}		\
		--config-dir ${ETCDIR}		\
		--cgi-dir ${CGIDIR}		\
		--data-dir /var/db/BackupPC	\
		--dest-dir ${STAGEDIR}		\
		--fhs				\
		--html-dir ${WWWDIR}		\
		--html-dir-url /${PORTNAME}	\
		--install-dir ${PREFIX}		\
		--log-dir /var/log/BackupPC	\
		--no-set-perms			\
		--uid-ignore

	pod2man --section=1 --release=${PORTVERSION} \
		--name=BackupPC --center="BackupPC user guide" \
		${WRKSRC}/doc/BackupPC.pod ${WRKSRC}/${PORTNAME}.1
	${INSTALL_MAN} ${WRKSRC}/${PORTNAME}.1 ${STAGEDIR}${PREFIX}/share/man/man1
	cd ${WRKSRC} && ${INSTALL_DATA} ${PORTDOCS} ${STAGEDIR}${DOCSDIR}
	${CP} ${WRKSRC}/doc/BackupPC.html ${STAGEDIR}${WWWDIR}
	${RM} ${STAGEDIR}${ETCDIR}/config.pl
	${RM} ${STAGEDIR}${ETCDIR}/hosts
	${CP} ${WRKDIR}/update.sh ${STAGEDIR}${ETCDIR}/update.sh
	${MKDIR} ${STAGEDIR}${PREFIX}/libexec/backuppc
	${CP} ${WRKSRC}/configure.pl ${STAGEDIR}${PREFIX}/libexec/backuppc/configure.pl

.include <bsd.port.mk>
