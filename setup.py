from distutils.core import setup, Extension

dme_sources = [
     "DolphinProcess/DolphinAccessor.cpp",
     "Common/MemoryCommon.cpp",
     "MemoryWatch/MemWatchEntry.cpp",
     "MemoryWatch/MemWatchTreeNode.cpp",
     "CheatEngineParser/CheatEngineParser.cpp",
     "MemoryScanner/MemoryScanner.cpp"
]

internal = CMakeExtension('wiirpcinternal',
                    sources = dme_sources)

setup(name="wiirpc", version="0.1", description="Discord Rich Presence for Wii Games", ext_modules=[internal])
