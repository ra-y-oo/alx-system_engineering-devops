# /etc/puppetlabs/code/environments/production/modules/apache500fix/manifests/init.pp
class apache500fix {
  file { '/etc/httpd/conf.d/vhost.conf':
    ensure  => 'file',
    content => template('apache500fix/vhost.conf.erb'),
    notify  => Service['httpd'],
  }
}
