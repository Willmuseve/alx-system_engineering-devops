# new file

file { '/tmp/school':
  ensure  => 'admin',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
