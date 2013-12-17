Converting .ui files into .py files
------------------------------------------
Just run ui2py.bat

Packaging req_extractor.exe with pyinstaller
--------------------------------------------
Go to the pyinstaller directory
python Configure.py
python Maksespec.py <path>/req_extractor.py
python MakeComServer.py <path>/req_extractor.py
python Build.py req_extractor/req_extractor.spec
Then goto the req_extractor/dist/req_extractor directory and copy the documentation folder in it.
Finally, just make a zip with it and that's all, the program is ready for distribution.