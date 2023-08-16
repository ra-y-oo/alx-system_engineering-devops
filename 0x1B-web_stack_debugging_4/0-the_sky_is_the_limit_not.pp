
class web_server {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure    => 'running',
    enable    => true,
    subscribe => File['/etc/nginx/nginx.conf'],
  }

  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('web_server/nginx.conf.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

include web_server
