// vim: set filetype=groovy:

def image_name = "registry.finn-thorben.me/homepage"

pipeline {
    agent {
        kubernetes {
            yaml """
kind: Pod
spec:
  containers:
    - name: jnlp
      image: "docker.io/jenkins/inbound-agent"
      args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
    - name: kustomize
      image: docker.io/nekottyo/kustomize-kubeval
      tty: true
      command:
      - cat
    - name: podman
      image: quay.io/podman/stable
      tty: true
      securityContext:
        runAsUser: 1000
        privileged: true
      command:
        - cat
    - name: node
      image: docker.io/node:16-alpine
      tty: true
      command:
        - cat
"""
        }
    }
    options {
        skipDefaultCheckout(true)
    }
    triggers {
      pollSCM 'H * * * *'
    }
    stages {
        stage("Checkout SCM") {
            steps {
                checkout scm
            }
        }
        stage("Build Kustomization") {
            steps {
                container("kustomize") {
                    sh "kustomize build . > k8s.yml"
                }
            }
        }
        stage("Check Kubernetes Config validity") {
            steps {
                container("kustomize") {
                    sh "kubeval k8s.yml --strict"
                }
            }
        }
        stage("Run linters") {
            steps {
                container("node") {
                    dir("src") {
                        sh "yarn install --pure-lockfile"
                        sh "yarn run lint"
                    }
                }
            }
        }
        stage("Build Container Image") {
            steps {
                container("podman") {
                    sh "podman build -t $image_name ."
                }
            }
        }
        stage("Upload Container Image") {
            when {
                beforeAgent true
                not { changeRequest() } 
            }
            steps {
                container("podman") {
                    milestone(ordinal: 100)
                    withCredentials([usernamePassword(credentialsId: 'registry-credentials', passwordVariable: 'registry_password', usernameVariable: 'registry_username')]) {
                        sh "podman login registry.finn-thorben.me -u $registry_username -p $registry_password"
                    }
                    sh "podman push $image_name"
                }
            }
        }
    }
}

