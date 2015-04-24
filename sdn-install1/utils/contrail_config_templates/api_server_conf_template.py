import string

template = string.Template("""
[DEFAULTS]
ifmap_server_ip=$__contrail_ifmap_server_ip__
ifmap_server_port=$__contrail_ifmap_server_port__
ifmap_username=$__contrail_ifmap_username__
ifmap_password=$__contrail_ifmap_password__
cassandra_server_list=$__contrail_cassandra_server_list__
listen_ip_addr=$__contrail_listen_ip_addr__
listen_port=$__contrail_listen_port__
auth=keystone
multi_tenancy=$__contrail_multi_tenancy__
log_file=$__contrail_log_file__
disc_server_ip=$__contrail_disc_server_ip__
disc_server_port=$__contrail_disc_server_port__
zk_server_ip=$__contrail_zookeeper_server_ip__
redis_server_ip=$__contrail_redis_ip__
rabbit_server=$__rabbit_server_ip__
rabbit_port=$__rabbit_server_port__

[SECURITY]
use_certs=$__contrail_use_certs__
keyfile=$__contrail_keyfile_location__
certfile=$__contrail_certfile_location__
ca_certs=$__contrail_cacertfile_location__

[KEYSTONE]
auth_host=$__contrail_keystone_ip__
auth_protocol=$__contrail_ks_auth_protocol__
auth_port=$__contrail_ks_auth_port__
admin_user=$__contrail_admin_user__
admin_password=$__contrail_admin_password__
admin_token=$__contrail_admin_token__
admin_tenant_name=$__contrail_admin_tenant_name__
insecure=$__keystone_insecure_flag__
$__contrail_memcached_opt__
""")
