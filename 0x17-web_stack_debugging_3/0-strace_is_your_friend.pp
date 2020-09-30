# Puppet manifesto
exec { 'error fix':
  path     => ['/bin', '/usr/bin', '/usr/sbin'],
  provider => 'shell',
  command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
