(defproject wordcount "0.0.1-SNAPSHOT"
  :resource-paths ["_resources"]
  :target-path "_build"
  :min-lein-version "2.0.0"
  :jvm-opts ["-client"]
  :repositories { "HDP Releases" "http://repo.hortonworks.com/content/repositories/releases" }
  :dependencies  [[org.apache.storm/storm-core "0.10.0.2.3.2.0-2950"]
                  [org.apache.storm/flux-core "0.10.0.2.3.2.0-2950"]]
  :jar-exclusions     [#"log4j\.properties" #"org\.apache\.storm\.(?!flux)" #"trident" #"META-INF" #"meta-inf" #"\.yaml"]
  :uberjar-exclusions [#"log4j\.properties" #"org\.apache\.storm\.(?!flux)" #"trident" #"META-INF" #"meta-inf" #"\.yaml"]
  )
  ;; never do this
    (require 'cemerick.pomegranate.aether)
    (cemerick.pomegranate.aether/register-wagon-factory!
     "http" #(org.apache.maven.wagon.providers.http.HttpWagon.))
