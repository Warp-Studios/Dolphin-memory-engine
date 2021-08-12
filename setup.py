from distutils.core import setup, Extension

dme_sources = [
     "Source/DolphinProcess/DolphinAccessor.cpp",
     "Source/Common/MemoryCommon.cpp",
     "Source/MemoryWatch/MemWatchEntry.cpp",
     "Source/MemoryWatch/MemWatchTreeNode.cpp",
     "SourceCheatEngineParser/CheatEngineParser.cpp",
     "Source/MemoryScanner/MemoryScanner.cpp"
]

internal = Extension('wiirpcinternal',
                    sources = dme_sources)

setup(name="wiirpc", version="0.1", description="Discord Rich Presence for Wii Games", ext_modules=[internal])
