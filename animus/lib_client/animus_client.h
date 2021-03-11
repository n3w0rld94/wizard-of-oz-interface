/* Code generated by cmd/cgo; DO NOT EDIT. */

/* package github.com/Cyberselves/AnimusClient */


#line 1 "cgo-builtin-export-prolog"

#include <stddef.h> /* for ptrdiff_t below */

#ifndef GO_CGO_EXPORT_PROLOGUE_H
#define GO_CGO_EXPORT_PROLOGUE_H

#ifndef GO_CGO_GOSTRING_TYPEDEF
typedef struct { const char *p; ptrdiff_t n; } _GoString_;
#endif

#endif

/* Start of preamble from import "C" comments.  */


#line 10 "client_exported.go"

	#include <stdio.h>
	#include <stdlib.h>
	#include <inttypes.h>
	#include <stdint.h>
	#include <string.h>
	#include <stdbool.h>

	typedef struct {
		size_t len;
		void* data;
	} ProtoMessageC;

#line 1 "cgo-generated-wrapper"


/* End of preamble from import "C" comments.  */


/* Start of boilerplate cgo prologue.  */
#line 1 "cgo-gcc-export-header-prolog"

#ifndef GO_CGO_PROLOGUE_H
#define GO_CGO_PROLOGUE_H

typedef signed char GoInt8;
typedef unsigned char GoUint8;
typedef short GoInt16;
typedef unsigned short GoUint16;
typedef int GoInt32;
typedef unsigned int GoUint32;
typedef long long GoInt64;
typedef unsigned long long GoUint64;
typedef GoInt64 GoInt;
typedef GoUint64 GoUint;
#ifndef SWIG
typedef __SIZE_TYPE__ GoUintptr;
#endif
typedef float GoFloat32;
typedef double GoFloat64;
#ifndef SWIG
typedef float _Complex GoComplex64;
#endif
#ifndef SWIG
typedef double _Complex GoComplex128;
#endif

/*
  static assertion to make sure the file is being used on architecture
  at least with matching size of GoInt.
*/
typedef char _check_for_64_bit_pointer_matching_GoInt[sizeof(void*)==64/8 ? 1:-1];

#ifndef GO_CGO_GOSTRING_TYPEDEF
typedef _GoString_ GoString;
#endif
typedef void *GoMap;
typedef void *GoChan;
typedef struct { void *t; void *v; } GoInterface;
typedef struct { void *data; GoInt len; GoInt cap; } GoSlice;

#endif

/* End of boilerplate cgo prologue.  */

#ifdef __cplusplus
extern "C" {
#endif


extern char* VersionGo();

//TODO use SetupComplete parameter

extern ProtoMessageC SetupGo(ProtoMessageC p0);

extern ProtoMessageC LoginUserGo(ProtoMessageC p0);

extern ProtoMessageC GetRobotsGo(ProtoMessageC p0);

extern ProtoMessageC ConnectGo(ProtoMessageC p0);

extern ProtoMessageC OpenModalityGo(char* p0, ProtoMessageC p1);

extern ProtoMessageC SetModalityGo(char* p0, char* p1, int p2, ProtoMessageC p3);

extern ProtoMessageC GetModalityGo(char* p0, char* p1, int p2);

extern ProtoMessageC CloseModalityGo(char* p0, char* p1);

extern ProtoMessageC DisconnectGo(char* p0);

extern void CloseClientInterfaceGo();

#ifdef __cplusplus
}
#endif