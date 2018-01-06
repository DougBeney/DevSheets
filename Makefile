# Builds an executable
build: clean
	pyinstaller main.py\
		--hidden-import pyexcel_io.readers.csvr\
		--hidden-import pyexcel_io.readers.csvz\
		--hidden-import pyexcel_io.readers.tsv\
		--hidden-import pyexcel_io.readers.tsvz\
		--hidden-import pyexcel_io.writers.csvw\
		--hidden-import pyexcel_io.readers.csvz\
		--hidden-import pyexcel_io.readers.tsv\
		--hidden-import pyexcel_io.readers.tsvz\
		--hidden-import pyexcel_io.database.importers.django\
		--hidden-import pyexcel_io.database.importers.sqlalchemy\
		--hidden-import pyexcel_io.database.exporters.django\
		--hidden-import pyexcel_io.database.exporters.sqlalchemy\
		--hidden-import pyexcel.plugins.renderers.sqlalchemy\
		--hidden-import pyexcel.plugins.renderers.django\
		--hidden-import pyexcel.plugins.renderers.excel\
		--hidden-import pyexcel.plugins.renderers._texttable\
		--hidden-import pyexcel.plugins.parsers.excel\
		--hidden-import pyexcel.plugins.parsers.sqlalchemy\
		--hidden-import pyexcel.plugins.sources.http\
		--hidden-import pyexcel.plugins.sources.file_input\
		--hidden-import pyexcel.plugins.sources.memory_input\
		--hidden-import pyexcel.plugins.sources.file_output\
		--hidden-import pyexcel.plugins.sources.output_to_memory\
		--hidden-import pyexcel.plugins.sources.pydata.bookdict\
		--hidden-import pyexcel.plugins.sources.pydata.dictsource\
		--hidden-import pyexcel.plugins.sources.pydata.arraysource\
		--hidden-import pyexcel.plugins.sources.pydata.records\
		--hidden-import pyexcel.plugins.sources.django\
		--hidden-import pyexcel.plugins.sources.sqlalchemy\
		--hidden-import pyexcel.plugins.sources.querysets
	mv dist/main dist/dougsheets

# Installs to a Linux system
install_unix:
	if [ -d "/opt/dougsheets" ]; then sudo rm -rf /opt/dougsheets; fi
	sudo cp -r dist/ /opt/dougsheets
	if [ -d "/usr/bin/dougsheets" ]; then sudo rm /usr/bin/dougsheets; fi
	sudo ln -sf /opt/dougsheets/dougsheets/main /usr/bin/dougsheets
	if [ -d "/etc/dougsheets" ]; then sudo rm -rf /etc/dougsheets; fi
	sudo mkdir /etc/dougsheets
	sudo cp -r sysplugins/ /etc/dougsheets/
	sudo rm -rf /etc/dougsheets/sysplugins/__pycache__

	mkdir -p ~/.config/dougsheets
	cp -r examples/ ~/.config/dougsheets

# Windows-related variables
WINDOWS_dougsheets = $(APPDATA)/WINDOWS_dougsheets
WINDOWS_sysplugins = $(WINDOWS_dougsheets)/WINDOWS_sysplugins
WINDOWS_userplugins = $(WINDOWS_dougsheets)/plugins

install_windows:
	if [ -d "$(WINDOWS_sysplugins)" ]; then rm -rf $(WINDOWS_sysplugins); fi
	mkdir -p $(WINDOWS_dougsheets)
	mkdir -p $(WINDOWS_userplugins)
	cp -rf dist/WINDOWS_dougsheets $(WINDOWS_dougsheets)/app
	cp -r WINDOWS_sysplugins $(WINDOWS_dougsheets)

# Deletes build files
clean:
	rm -rf build/ dist/ *.spec

