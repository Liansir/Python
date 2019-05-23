# kubernetes离线安装

- kubernetes1.9.0离线安装

- kubeadm是kubernetes官方推荐的自动化部署工具

- 1个master，2个node节点

- 部署前进行卸载清理

  - ```shell
    yum -y remove kubernetes*  docker* docker-selinux etcd
    ```

- 部署前要进行ssh互信、关闭防火墙、selinux、配置内核参数

  - ```shell
    # ssh-keygen 
    # ssh-copy-id -i /root/.ssh/id_rsa.pub  root@vm2
    # scp -rp k8s_images vm2:/root
    ```

    ```
    # systemctl stop firewalld && systemctl disable firewalld 
    # getenforce 
    Disabled
    # echo "
    net.bridge.bridge-nf-call-ip6tables = 1
    net.bridge.bridge-nf-call-iptables = 1
    " >> /etc/sysctl.conf
    # sysctl -p
    
    ```

- 安装docker-ce(17.03)并导入kubeadm image文件

  - ```shell
    # 解压镜像
    # yum install bzip2
    # tar -xjvf k8s_images.tar.bz2 
    # cd k8s_images
    # yum -y localinstall docker-ce-*
    
    # systemctl start docker && systemctl enable docker
    # docker version
    # 导入镜像
    # cd k8s_images/docker_images/
    # for i in $(ls *.tar);do docker load < $i;done
    # cd ..
    # docker load < kubernetes-dashboard_v1.8.1.tar 
    # 检查镜像
    # docker images |grep google
    ```

  - image文件检验

    - ```shell
      md5sum k8s_images.tar.bz2
      b60ad6a638eda472b8ddcfa9006315ee
      ```

- master和node同步安装k8s 1.9.0

  - ```shell
    # cd /root/k8s_images/
    # rpm -ivh socat-1.7.3.2-2.el7.x86_64.rpm
    # rpm -ivh kubernetes-cni-0.6.0-0.x86_64.rpm \
     kubelet-1.9.9-9.x86_64.rpm  \
    kubectl-1.9.0-0.x86_64.rpm
    # rpm -ivh kubectl-1.9.0-0.x86_64.rpm
    # rpm -ivh kubeadm-1.9.0-0.x86_64.rpm
    # rpm -qa |grep kube
    # rpm -qa |grep socat
    ```

  - 