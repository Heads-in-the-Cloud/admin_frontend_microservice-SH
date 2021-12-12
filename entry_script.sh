#!/bin/bash
set -e

file_env() {
	var="$1"
	fileVar="${var}_FILE"
	def="nada"
	if [[ -f "${fileVar}" ]]; then
	  val="$(cat "${fileVar}")"
	elif [[ -z ${var} ]]; then
	  val="${var}"
	else
		val="$def"
	fi
	export "$var"="$val"
	unset "$fileVar"
}

if [[ -n $SECRET_KEY || -n $SECRET_KEY_FILE ]]; then
  file_env 'SECRET_KEY'
fi

export JWT_SECRET_KEY="$SECRET_KEY"

python /app/app.py