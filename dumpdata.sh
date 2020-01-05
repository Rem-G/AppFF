#! /bin/sh

python3 manage.py dumpdata --indent 2 --exclude auth --exclude sessions --exclude contenttypes --exclude admin > dump_test.json