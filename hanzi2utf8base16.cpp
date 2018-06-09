   char str[]="¿¿¿";// ansi
    char str8[20]="0";
    int  len=9;//
    WCHAR  wBuf[20]={0};
    MultiByteToWideChar(CP_ACP,0,str,len,wBuf,len);// ansi 2 unicode
    WideCharToMultiByte(CP_UTF8,0,wBuf,len,str8,len,0,0);// unicode to utf8
//str8="E4 B8 81 E4 B8 80 E4 B8 87"
    len=strlen(str8);
    CString tmp="";
    CString Out="";
    for(int jj=0;jj<len;jj++)
    {
        tmp.Format("%02X ",(BYTE)str8[jj]);
        Out+=tmp;
    }
    afxDump << Out << "\n";
