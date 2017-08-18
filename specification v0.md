__.cif (Custom Image Format) file specification v0__
================================================

Header
------
+ __format version__ - *uint8_t* (counting up start at 0) <br>
+ __image width__ - *uint16_t* <br>
+ __image height__ - *uint16_t* <br>
+ __comment length in bytes__ - *uint8_t* <br>
+ __comment__ - *ascii encoding*, length variable (see *__comment length in bytes__*)

Image data
----------
+ __information per pixel__ - *3 bytes* (RGB value)

ToDo in next version(s)
-----------------------
+ __image data compression__ *(gzip?)*
