# NagBody configure.ac file - MathematicaMCMC code
# Copyright (c) 2006-2019  Mario A. Rodriguez-Meza, Ciudad de Mexico.
#
#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([MathematicaMCMC], [1.0], [marioalberto.rodriguezmeza@gmail.com])

AM_INIT_AUTOMAKE(silent-rules)
AM_SILENT_RULES
# The following trajectory is important to find install-sh for instance.
AC_CONFIG_SRCDIR([Mathematica/mcmc/MathematicaMCMC/MathematicaMCMC.nb])
AC_CONFIG_HEADERS([config.h])

AC_PREFIX_DEFAULT(/usr/local/NagBody)

# Checks for programs.
# CC is defined by
AC_PROG_CC
#AC_PROG_F77(f90)
# FC is defined by
AC_PROG_FC
AC_PROG_INSTALL
AC_PROG_RANLIB
AC_PROG_CXX

dnl +------------------------------------------------
dnl | Check for Python
dnl +------------------------------------------------
#AC_LANG_PUSH([C])
#toast_python=yes
#AC_ARG_ENABLE(python, [AC_HELP_STRING([--disable-python], [Disable python bindings])], #[toast_python=$enable_python])
#if test $toast_python = yes; then
#  AM_PATH_PYTHON(,[PYTHON_FOUND=yes],[PYTHON_FOUND=no])
#  if test $PYTHON_FOUND=yes; then
#    AX_PYTHON_DEVEL([>= '3.3.0'])
#  fi
#  if test "x$PYTHON" = "x"; then
#    toast_python=no
#  fi
#fi
#AC_LANG_POP([C])
#AM_CONDITIONAL([HAVE_AM_PYTHON], [test $toast_python = yes])


# Tell automake that this is not a GNU package (and doesn't need NEWS,
# AUTHORS, etc. files)
#AM_INIT_AUTOMAKE([foreign])

# Prevent Makefile from re-running automake etc automatically because
# it always uses the wrong version or doesn't use the necessary flags.
AM_MAINTAINER_MODE

# Checks for libraries.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for command-line options

# Checks for header files.
AC_CHECK_HEADERS([sys/param.h sys/timeb.h])

AC_CHECK_FUNCS([floor strstr pow sqrt strchr strdup])
# Needed by wrapper_wmap in montepython
AC_CHECK_FUNCS([getcwd])
AC_CHECK_FUNCS([memset])
AC_CHECK_FUNCS([strerror])


AC_C_INLINE
AC_C_RESTRICT
AC_FUNC_REALLOC

AC_CHECK_HEADER_STDBOOL
AC_FUNC_ERROR_AT_LINE
AC_FUNC_MALLOC
AC_TYPE_SIZE_T

# Defining variables to be passed on the compiler via DEFS substitution variable
AC_DEFINE(NOGNU, [1], [Description])
#AC_DEFINE_UNQUOTED(NOGNU)


AC_CONFIG_FILES([Makefile
		doc/Makefile
		doc/mcmc/Makefile
		doc/mcmc/MathematicaMCMC/Makefile])


AC_OUTPUT

echo \
"-------------------------------------------------------
${PACKAGE_NAME} Version ${PACKAGE_VERSION}
Prefix: '${prefix}'.
compiler: '${CC} ${CFLAGS} ${CPPFLAGS}'

Package features:
  Async Execution: ${async_exec}

Now type 'make @<:@<target>@:>@'
  where the optional <target> is:
    all			- build all binaries
    install		- install everything

-------------------------------------------------------"


