class user_limit {
  user { 'holberton':
    ensure => present,
    managehome => true,
    shell => '/bin/bash', # Set the desired shell for the user
    uid => 1001,          # Set a unique UID for the user
    gid => 1001,          # Set a primary GID for the user
    home => '/home/holberton', # Set the home directory path
  }

  file { '/home/holberton/sample_file.txt':
    ensure => file,
    owner => 'holberton',
    group => 'holberton',
    mode => '0644',
    content => 'This is a sample file.',
  }
}

include user_limit
