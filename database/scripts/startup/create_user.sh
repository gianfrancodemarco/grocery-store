echo "CREATE USER $ORACLE_USER IDENTIFIED BY $ORACLE_PASSWORD;
GRANT ALL PRIVILEGES TO $ORACLE_USER;
exit
" | sqlplus SYS/password@ORCLCDB AS SYSDBA
