resource "aws_eks_node_group" "example" {
  cluster_name    = aws_eks_cluster.eks_cluster.name
  node_group_name = "example-node-group"
  node_role_arn   = aws_iam_role.eks_worker_role.arn
  subnet_ids      = [aws_subnet.eks_subnet1.id, aws_subnet.eks_subnet2.id]

  scaling_config {
    desired_size = 10
    max_size     = 12
    min_size     = 10
  }

  # Use the latest EKS optimized AMI for Amazon Linux 2
  ami_type = "AL2_x86_64"

  # Specify instance type
  instance_types = ["t3.medium"]

  # Ensure the Kubernetes version matches your EKS cluster version
  version = aws_eks_cluster.eks_cluster.version

  # Additional configurations can be set here (e.g., labels, taints)

  depends_on = [
    aws_iam_role_policy_attachment.eks_worker_AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.eks_worker_AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.eks_worker_AmazonEC2ContainerRegistryReadOnly,
  ]
}
