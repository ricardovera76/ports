PORTNAME=	pgsphere
PORTVERSION=	1.1.5
PORTREVISION=	4
CATEGORIES=	databases geography

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Spherical data types, functions, and operators for PostgreSQL
WWW=		https://pgsphere.github.io/

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/COPYRIGHT.pg_sphere

DEPRECATED=	The repository has been archived by the owner on 2023-08-09 and is inactive for almost 4.5 years
EXPIRATION_DATE=2024-04-30

OPTIONS_DEFINE=	DOCS

USES=		gmake pgsql
LLD_UNSAFE=	yes
USE_LDCONFIG=	yes
MAKE_ARGS=	PG_CONFIG=${LOCALBASE}/bin/pg_config USE_PGXS=1 \
		docdir=${DOCSDIR} \
		install_bin=/usr/bin/install
TEST_TARGET=	installcheck

DATADIR=	${PREFIX}/share/postgresql
DOCSDIR?=	${PREFIX}/share/doc/postgresql

GH_TAGNAME=	e0b303d
USE_GITHUB=	yes

DOCS_MAKE_ARGS_OFF=	DOCS=""

post-patch:
	@${REINPLACE_CMD} -e 's|int4|int32|g' ${WRKSRC}/line.c ${WRKSRC}/line.h

post-install:
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/lib/postgresql/pg_sphere.so

.include <bsd.port.mk>
