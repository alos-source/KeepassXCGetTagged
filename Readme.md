# Export Tagged Entries
## Description
This is a script controlling KeePassXC via it's cli. The script aims to export all entries carrying a specific tag, without exporting the actual password.
The original usecase is: Create lists of services and login names, for all services relevant for your digital legacy. So the definition of relevant services can be done in the actual database, using a specific tag e.g. #digitallegacy.

## Use-Case / Why i've done this?
I've been thinking about, how to pass on information about relevant online services and passwords as part of my legacy. Of course I don't want to create an additional list of services and login data, but use my existing database. So i added the tag #digitallegacy to a couple of relevent entries of my password database. Unfortunatelly KeePassXC does not support options for export like *filtered export*. So i took a workaround using the KeePassXC cli, to read all entries matching the #tag pattern and exporting them as a csv-list.
The clear text password is left out here intentionally, since it will propably change anyway and with official documents should also get access.

## Requirements
The program is designed for use with KeePassXC. It most likly not work with other derivates of keepass.
Testet using *KeePassXC - Version 2.7.6* and *Windows 11 Version 2009*.

## References
As a reference for KeePassXC cli see documentation: https://github.com/keepassxreboot/keepassxc/blob/develop/docs/man/keepassxc-cli.1.adoc