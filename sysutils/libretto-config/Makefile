PORTNAME=	libretto-config
PORTVERSION=	1.0.b5
PORTREVISION=	10
CATEGORIES=	sysutils
MASTER_SITES=	http://club.pep.ne.jp/~ishioka/Software/Linux/libapm/
DISTNAME=	libapm-linux-1.0beta5

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Libretto BIOS Setting Program

BROKEN=		Unfetchable
DEPRECATED=	Utility for obsolete hardware released 20 years ago
EXPIRATION_DATE=2024-04-30

ONLY_FOR_ARCHS=	i386

WRKSRC=		${WRKDIR}/libapm

USE_GCC=	yes
PORTDOCS=	*

MAKE_ARGS=	MANDIR=${PREFIX}/share/man

OPTIONS_DEFINE=	DOCS

post-install:
	${MkDIR} ${STAGEDIR}${PREFIX}/share/man/ja/man8
	${INSTALL_MAN} ${WRKSRC}/libapm-j.man ${STAGEDIR}${PREFIX}/share/man/ja/man8/${PORTNAME}.8

post-install-DOCS-on:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/README-e.1st ${STAGEDIR}${DOCSDIR}/README.1st
	${INSTALL_DATA} ${WRKSRC}/APM-EXBIOS-e.txt ${STAGEDIR}${DOCSDIR}/APM-EXBIOS.txt
	@${MKDIR} ${STAGEDIR}${DOCSDIR}/ja
	${INSTALL_DATA} ${WRKSRC}/README-j.1st ${STAGEDIR}${DOCSDIR}/ja/README.1st
	${INSTALL_DATA} ${WRKSRC}/APM-EXBIOS-j.txt ${STAGEDIR}${DOCSDIR}/ja/APM-EXBIOS.txt

.include <bsd.port.mk>
