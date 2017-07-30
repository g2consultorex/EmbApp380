

import tempfile
import win32api
import win32print

#filename = tempfile.mktemp ("C:\\Proyectos\\NOM004.txt")
filename = ("C:\\Proyectos\\ZE_102466.pdf")
# open (filename, "w").write ("This is a test, This is a test, This is a test, This is a test, This is a test, " +
# 	 "This is a test, This is a test, This is a test, This is a test")
#print (filename)


print win32print.GetDefaultPrinter()

win32api.ShellExecute (
  0,
  "print",
  filename,
  #
  # If this is None, the default printer will
  # be used anyway.
  #
  '/d:"%s"' % win32print.GetDefaultPrinter(),
  ".",
  0
)

