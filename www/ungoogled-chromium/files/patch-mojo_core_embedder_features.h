--- mojo/core/embedder/features.h.orig	2022-10-01 07:40:07 UTC
+++ mojo/core/embedder/features.h
@@ -14,7 +14,7 @@ namespace mojo {
 namespace core {
 
 #if BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_NACL) && !BUILDFLAG(IS_MAC)
-#if BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_ANDROID)
+#if BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_ANDROID) || BUILDFLAG(IS_BSD)
 COMPONENT_EXPORT(MOJO_CORE_EMBEDDER_FEATURES)
 extern const base::Feature kMojoLinuxChannelSharedMem;
 