# Analysis Results

For each implemented attack, the results obtained by the tools are provided.
In each present directory it is possible to find:

- `dockle-results-{attack-type}.json`: Dockle results reporting any container discrepancies against the CIS Docker Community Edition Benchmarks;
- `grype-results-{attack-type}.json`: Grype results of vulnerabilities for images and container filesystems;
- `snyk-code-break-{attack-type}.log`: Snyk's results of static code analysis;
- `snyk-container-{attack-type}.log`: Snyk results reporting any package vulnerabilities by performing a container analysis;
- `snyk-unmanaged-{attack-type}.log`: Snyk results of the analysis of dependencies, issues or vulnerabilities in the code;
- `trivy-compliance-{attack-type}.log`: Trivy results of the analysis for compliance with reference to CIS Docker Community Edition Benchmarks;
- `trivy-image-{attack-type}.log`: Trivy results on the analysis of Dockerfile "best-practices";
- `trivy-secrets-{attack-type}.log`: Trivy results on the analysis of any secrets present in the containers;
- `trivy-scanners-{attack-type}.log`: Trivy results for any vulnerabilities detected. 

