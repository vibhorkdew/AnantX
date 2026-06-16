================================================================================
                                KAVACHOPS
      AI-Powered Cloud-Native DevSecOps & Threat Intelligence Platform
================================================================================

                                ┌──────────────────────┐
                                │      END USERS       │
                                │──────────────────────│
                                │ • Security Analysts  │
                                │ • DevOps Engineers   │
                                │ • Developers         │
                                │ • Admins             │
                                └──────────┬───────────┘
                                           │
                                    HTTPS / TLS
                                           │
                                           ▼
================================================================================
                           EDGE & ACCESS LAYER
================================================================================

                            ┌──────────────────┐
                            │    CLOUDFLARE    │
                            │──────────────────│
                            │ • DDoS Protection│
                            │ • CDN            │
                            │ • WAF            │
                            │ • Rate Limiting  │
                            └────────┬─────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │      NGINX       │
                            │──────────────────│
                            │ Reverse Proxy    │
                            │ SSL Termination  │
                            │ API Routing      │
                            │ Security Headers │
                            │ Request Filtering│
                            └────────┬─────────┘
                                     │
                                     ▼
================================================================================
                             FRONTEND LAYER
================================================================================

                     ┌──────────────────────────────┐
                     │       REACT DASHBOARD        │
                     │──────────────────────────────│
                     │ • Login UI                   │
                     │ • Security Dashboard         │
                     │ • Threat Monitoring          │
                     │ • Vulnerability Reports      │
                     │ • Kubernetes Monitoring      │
                     │ • AI Security Assistant      │
                     │ • Incident Timeline          │
                     │ • CI/CD Pipeline Status      │
                     │ • Grafana Embedded Panels    │
                     └──────────────┬───────────────┘
                                    │
                              REST APIs
                                    │
                                    ▼
================================================================================
                            API GATEWAY LAYER
================================================================================

                       ┌────────────────────────┐
                       │     API GATEWAY        │
                       │────────────────────────│
                       │ • JWT Validation       │
                       │ • RBAC Enforcement     │
                       │ • Rate Limiting        │
                       │ • Request Authentication│
                       │ • API Routing          │
                       │ • Logging              │
                       └──────────┬─────────────┘
                                  │
================================================================================
                        MICROSERVICES LAYER
================================================================================

 ┌────────────────────────────────────────────────────────────────────────────┐
 │                                                                            │
 │  ┌────────────────┐     ┌────────────────┐     ┌────────────────────┐     │
 │  │ AUTH SERVICE   │     │ USER SERVICE   │     │ ALERT SERVICE      │     │
 │  │────────────────│     │────────────────│     │────────────────────│     │
 │  │ • JWT Auth     │     │ • User Mgmt    │     │ • Alert Mgmt       │     │
 │  │ • RBAC         │     │ • Role Mgmt    │     │ • Notifications    │     │
 │  │ • Login Logs   │     │ • Profile APIs │     │ • Severity Mgmt    │     │
 │  └──────┬─────────┘     └──────┬─────────┘     └──────────┬─────────┘     │
 │         │                      │                           │               │
 │         ▼                      ▼                           ▼               │
 │  ┌────────────────────────────────────────────────────────────────────┐    │
 │  │                    AI ANALYSIS SERVICE                             │    │
 │  │────────────────────────────────────────────────────────────────────│    │
 │  │ • AI Threat Analysis                                              │    │
 │  │ • Log Summarization                                               │    │
 │  │ • CVE Explanation                                                 │    │
 │  │ • Incident Classification                                         │    │
 │  │ • Threat Severity Prediction                                      │    │
 │  │ • AI Security Copilot                                             │    │
 │  └───────────────────────┬────────────────────────────────────────────┘    │
 │                          │                                                 │
 │                          ▼                                                 │
 │  ┌────────────────────────────────────────────────────────────────────┐    │
 │  │                    SCAN SERVICE                                    │    │
 │  │────────────────────────────────────────────────────────────────────│    │
 │  │ • Trivy Scanner Integration                                       │    │
 │  │ • Semgrep Integration                                             │    │
 │  │ • OWASP ZAP Integration                                           │    │
 │  │ • Vulnerability Aggregation                                       │    │
 │  │ • Security Report Generation                                      │    │
 │  └───────────────────────┬────────────────────────────────────────────┘    │
 │                          │                                                 │
 │                          ▼                                                 │
 │  ┌────────────────────────────────────────────────────────────────────┐    │
 │  │                 MONITORING SERVICE                                 │    │
 │  │────────────────────────────────────────────────────────────────────│    │
 │  │ • Metrics Collection                                              │    │
 │  │ • Log Aggregation                                                 │    │
 │  │ • Runtime Alert Collection                                        │    │
 │  │ • Dashboard APIs                                                  │    │
 │  │ • Incident Timeline                                               │    │
 │  └────────────────────────────────────────────────────────────────────┘    │
 │                                                                            │
 └────────────────────────────────────────────────────────────────────────────┘

================================================================================
                           DATA & MESSAGE LAYER
================================================================================

 ┌────────────────────┐    ┌────────────────────┐    ┌────────────────────┐
 │   POSTGRESQL DB    │    │       REDIS        │    │      RABBITMQ      │
 │────────────────────│    │────────────────────│    │────────────────────│
 │ • Users            │    │ • Cache            │    │ • Async Messaging  │
 │ • Vulnerabilities  │    │ • Sessions         │    │ • Event Queues     │
 │ • Alerts           │    │ • Rate Limiting    │    │ • Alert Pipelines  │
 │ • Incidents        │    │ • Token Storage    │    │ • Notification Bus │
 │ • Audit Logs       │    │                    │    │                    │
 └────────────────────┘    └────────────────────┘    └────────────────────┘

================================================================================
                        AI & INTELLIGENCE LAYER
================================================================================

                       ┌───────────────────────────┐
                       │          OLLAMA           │
                       │───────────────────────────│
                       │ • Local LLM Runtime       │
                       │ • Log Analysis            │
                       │ • Threat Intelligence     │
                       │ • Incident Summarization  │
                       │ • Vulnerability Analysis  │
                       │ • AI Security Assistant   │
                       └────────────┬──────────────┘
                                    │
                                    ▼
                     ┌──────────────────────────────┐
                     │      AI RESPONSE ENGINE      │
                     │──────────────────────────────│
                     │ Input:                       │
                     │ • Falco Alerts               │
                     │ • Trivy Reports              │
                     │ • Loki Logs                  │
                     │ • Prometheus Metrics         │
                     │                              │
                     │ Output:                      │
                     │ • Threat Summary             │
                     │ • Attack Classification      │
                     │ • Severity Level             │
                     │ • Recommended Mitigation     │
                     └──────────────────────────────┘

================================================================================
                          DEVSECOPS PIPELINE
================================================================================

 Developer Push
        │
        ▼
 ┌────────────────────┐
 │      GITHUB        │
 └─────────┬──────────┘
           │ Webhook Trigger
           ▼
 ┌────────────────────────────────────────────────────────────┐
 │                        JENKINS                            │
 │────────────────────────────────────────────────────────────│
 │                                                            │
 │ Stage 1: Source Checkout                                   │
 │ Stage 2: Python Unit Tests                                 │
 │ Stage 3: Linting                                           │
 │ Stage 4: Semgrep SAST Scan                                 │
 │ Stage 5: SonarQube Analysis                                │
 │ Stage 6: Docker Image Build                                │
 │ Stage 7: Trivy Vulnerability Scan                          │
 │ Stage 8: OWASP ZAP Dynamic Scan                            │
 │ Stage 9: Push Docker Images                                │
 │ Stage 10: Kubernetes Deployment                            │
 │ Stage 11: Smoke Testing                                    │
 │                                                            │
 └──────────────┬─────────────────────────────────────────────┘
                │
                ▼
================================================================================
                        CONTAINERIZATION LAYER
================================================================================

                    ┌─────────────────────────┐
                    │         DOCKER          │
                    │─────────────────────────│
                    │ • FastAPI Containers    │
                    │ • React Container       │
                    │ • PostgreSQL Container  │
                    │ • Monitoring Containers │
                    │ • Jenkins Container     │
                    └────────────┬────────────┘
                                 │
                                 ▼
================================================================================
                       KUBERNETES CLUSTER LAYER
================================================================================

                  ┌─────────────────────────────────┐
                  │          K3D / K8S              │
                  └─────────────────────────────────┘

Namespaces:
───────────────────────────────────────────────────────────────────────────────

┌─────────────────────┐
│ app-namespace       │
│─────────────────────│
│ • FastAPI Pods      │
│ • React Pods        │
│ • API Gateway       │
└─────────────────────┘

┌─────────────────────┐
│ monitoring-namespace│
│─────────────────────│
│ • Prometheus        │
│ • Grafana           │
│ • Loki              │
└─────────────────────┘

┌─────────────────────┐
│ security-namespace  │
│─────────────────────│
│ • Falco             │
│ • Trivy             │
│ • Vault             │
│ • Kyverno           │
└─────────────────────┘

================================================================================
                         KUBERNETES SECURITY
================================================================================

 ┌────────────────────┐
 │      KYVERNO       │
 │────────────────────│
 │ Security Policies: │
 │ • No root pods     │
 │ • No privileged    │
 │ • Image validation │
 │ • Resource limits  │
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │   NETWORK POLICIES │
 │────────────────────│
 │ Restrict pod       │
 │ communication      │
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │       VAULT        │
 │────────────────────│
 │ Secret Management  │
 │ JWT Secrets        │
 │ DB Credentials     │
 │ API Keys           │
 └────────────────────┘

================================================================================
                        RUNTIME SECURITY LAYER
================================================================================

                      ┌────────────────────────┐
                      │         FALCO          │
                      │────────────────────────│
                      │ Runtime Threat Detection│
                      │ Suspicious Shells      │
                      │ Privilege Escalation   │
                      │ Malicious Processes    │
                      │ Container Exploits     │
                      └──────────┬─────────────┘
                                 │
                                 ▼
================================================================================
                        OBSERVABILITY LAYER
================================================================================

 ┌────────────────────┐    ┌────────────────────┐    ┌────────────────────┐
 │    PROMETHEUS      │    │       LOKI         │    │      GRAFANA       │
 │────────────────────│    │────────────────────│    │────────────────────│
 │ Metrics Collection │    │ Log Aggregation    │    │ Dashboards         │
 │ Pod Metrics        │    │ Application Logs   │    │ Threat Monitoring  │
 │ CPU/Memory         │    │ Security Logs      │    │ CI/CD Monitoring   │
 │ Alert Rules        │    │ Kubernetes Logs    │    │ Runtime Security   │
 └─────────┬──────────┘    └─────────┬──────────┘    └────────────────────┘
           │                         │
           └──────────────┬──────────┘
                          │
                          ▼
================================================================================
                      THREAT ANALYSIS FLOW
================================================================================

 Suspicious Activity
          │
          ▼
      Falco Alert
          │
          ▼
      Loki Logging
          │
          ▼
  AI Analysis Service
          │
          ▼
 Threat Classification
          │
          ▼
 Severity Assignment
          │
          ▼
 Grafana Dashboard Alert
          │
          ▼
 Security Analyst Action

================================================================================
                       SECURITY INCIDENT FLOW
================================================================================

 Attacker Attempts Brute Force
               │
               ▼
       Failed Login Spike
               │
               ▼
      Prometheus Alert Triggered
               │
               ▼
      Logs Stored in Loki
               │
               ▼
     AI Detects Attack Pattern
               │
               ▼
 Incident Summary Generated
               │
               ▼
 Dashboard Displays:
 • Threat Severity
 • Affected Service
 • Recommended Action
 • Attack Timeline

================================================================================
                        FINAL PROJECT OBJECTIVE
================================================================================

KavachOps provides an enterprise-grade AI-powered DevSecOps ecosystem
that integrates:

• CI/CD Security
• Container Security
• Kubernetes Security
• Runtime Threat Detection
• Vulnerability Analysis
• Security Observability
• AI-Powered Incident Intelligence
• Cloud-Native Monitoring
• Zero-Trust Security Principles

into a single intelligent security operations platform.

================================================================================
