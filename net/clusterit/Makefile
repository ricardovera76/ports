PORTNAME=	clusterit
PORTVERSION=	2.5
PORTREVISION=	1
CATEGORIES=	net devel parallel
MASTER_SITES=	SF/${PORTNAME}/${PORTNAME}/${PORTNAME}-${PORTVERSION}

MAINTAINER=	demon@FreeBSD.org
COMMENT=	Collection of clustering tools
WWW=		https://www.garbled.net/clusterit.html

LICENSE=	BSD2CLAUSE

GNU_CONFIGURE=	yes
GNU_CONFIGURE_MANPREFIX=	${PREFIX}/share

CONFLICTS_INSTALL=	barrier heirloom-sh pdsh schilyutils # bin/barrier bin/dshbak bin/jsh

OPTIONS_DEFINE=	X11
OPTIONS_SUB=	yes

X11_USES=	xorg
X11_USE=	XORG=x11

.include <bsd.port.options.mk>

post-patch-X11-off:
	${REINPLACE_CMD} -E 's,^(SUBDIRS) = .*,\1 = barrier dsh jsd pcp dtop tools,' ${WRKSRC}/Makefile.in

.include <bsd.port.mk>
