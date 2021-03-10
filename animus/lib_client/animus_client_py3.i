/* animus_client_py3.i */
%module animus_client_py3
%include typemaps.i
%include cdata.i

%begin %{
    #define SWIG_PYTHON_STRICT_BYTE_CHAR
%}

%{
   #include "animus_client.h"
%}

%pragma(java) jniclasscode=%{
  static {
    System.loadLibrary("animus_client");
  }
%}

%include "animus_client.h"

%inline %{

  SWIGCDATA Setup(char* p0, int p1) {
     ProtoMessageC protoreq = (ProtoMessageC) { p1, (void*)p0 };
     ProtoMessageC protoret = SetupGo(protoreq);
     return cdata_void(protoret.data, protoret.len);
  }

  SWIGCDATA LoginUser(char* p0, int p1) {
     ProtoMessageC protoreq = (ProtoMessageC) { p1, (void*)p0 };
     ProtoMessageC protoret = LoginUserGo(protoreq);
     return cdata_void(protoret.data, protoret.len);
  }

  SWIGCDATA GetRobots(char* p0, int p1) {
     ProtoMessageC protoreq = (ProtoMessageC) { p1, (void*)p0 };
     ProtoMessageC protoret = GetRobotsGo(protoreq);
     return cdata_void(protoret.data, protoret.len);
  }

  SWIGCDATA Connect(char* p0, int p1) {
     ProtoMessageC protoreq = (ProtoMessageC) { p1, (void*)p0 };
     ProtoMessageC protoret = ConnectGo(protoreq);
     return cdata_void(protoret.data, protoret.len);
  }

  SWIGCDATA OpenModality(char* p0, char* p1, int p2) {
     ProtoMessageC protoreq = (ProtoMessageC) { p2, (void*)p1 };
     ProtoMessageC protoret = OpenModalityGo(p0, protoreq);
     return cdata_void(protoret.data, protoret.len);
  }

  SWIGCDATA SetModality(char* p0, char* p1, int p2, char* p3, int p4) {
     ProtoMessageC protoreq = (ProtoMessageC) { p4, (void*)p3 };
     ProtoMessageC protoret = SetModalityGo(p0, p1, p2, protoreq);
     return cdata_void(protoret.data, protoret.len);
  }

  SWIGCDATA GetModality(char* p0, char* p1, int p2) {
     ProtoMessageC protoret = GetModalityGo(p0, p1, p2);
     return cdata_void(protoret.data, protoret.len);
  }

  SWIGCDATA CloseModality(char* p0, char* p1) {
     ProtoMessageC protoret = CloseModalityGo(p0, p1);
     return cdata_void(protoret.data, protoret.len);
  }

  SWIGCDATA Disconnect(char* p0) {
     ProtoMessageC protoret = DisconnectGo(p0);
     return cdata_void(protoret.data, protoret.len);
  }

%}

