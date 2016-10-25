import configuration

workload_list = "workloadmgr workload-list | grep available | wc -l"
snapshot_list = "workloadmgr snapshot-list | grep available | wc -l"
restore_list = "workloadmgr restore-list | grep available | wc -l"

workload_create = "workloadmgr workload-create --workload-type-id "+configuration.workload_type_id+\
                  " --display-name "+configuration.workload_name+\
                  " --source-platform "+configuration.source_platform
snapshot_create = "workloadmgr workload-snapshot " +configuration.workload_name+ " --full --display-name " +configuration.snapshot_name
snapshot_delete = "workloadmgr snapshot-delete " +configuration.snapshot_name
workload_delete = "workloadmgr workload-delete "+configuration.workload_name
delete_vm = "nova delete "
oneclick_restore = "workloadmgr snapshot-oneclick-restore --display-name " +configuration.restore_name
selective_restore = "workloadmgr snapshot-selective-restore --display-name " +configuration.selective_restore_name+ " --filename " +configuration.restore_filename
list_vm = "nova list | awk -F '|' '{print $2}' | grep -v ID"
workload_modify_name = "workloadmgr workload-modify --display-name "
workload_modify_description = "workloadmgr workload-modify --display-description "
