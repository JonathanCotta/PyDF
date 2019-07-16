@echo off

cd myenv/Scripts/

if "%1" == "-a" ( CALL activate )

if "%1" == "-d" ( CALL deactivate )

cd ..
cd ..

cls
