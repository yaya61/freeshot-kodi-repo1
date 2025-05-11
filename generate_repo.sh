#!/bin/bash

# Générer addons.xml
echo '<?xml version="1.0"?>' > repo/addons.xml
echo '<addons>' >> repo/addons.xml
cat plugin.video.freeshot/addon.xml >> repo/addons.xml
cat repo/repository.xml >> repo/addons.xml
echo '</addons>' >> repo/addons.xml

# Générer MD5
md5sum repo/addons.xml | awk '{print $1}' > repo/addons.xml.md5

# Créer le ZIP
zip -r repo/plugin.video.freeshot-1.0.0.zip plugin.video.freeshot/*
