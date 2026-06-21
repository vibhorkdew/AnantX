output "app_sg_id" {
  value = aws_security_group.app_sg.id
}

output "devsecops_sg_id" {
  value = aws_security_group.devsecops_sg.id
}

output "anantx_sg_id" {
  value = aws_security_group.anantx_sg.id
}
