# Week 04 — Docker & Containers
**Program:** TKH IFCS Phase One
**Sessions:** S10 · S11 · S12 "The Conductor & the Fleet" · TLAB-04 "Operation Hyper-Stack"
**Week Topic:** Virtualization concepts & multi-container architecture · Secure container configuration · Docker Compose deployment

---

## Session 10 — Virtualization Concepts & Multi-Container Architecture

### Summary

Session 10 introduced Docker and container-based virtualization as the infrastructure model underpinning the remainder of the program. The distinction between virtual machines and containers was established: VMs emulate an entire hardware stack and run a full OS, while containers share the host kernel and isolate only the process and its dependencies — making them faster to spin up, smaller in footprint, and more consistent across environments.

A `docker-compose.yml` was written to define a multi-container environment, specifying services, base images, environment variables, port mappings, and network assignments. The Compose file makes infrastructure declarative — what should exist is written down, and Docker builds it. This is the foundation of repeatable, auditable deployment: rather than a series of manual commands that exist only in someone's memory, the environment is defined as code and can be recreated identically at any time.

> **Note:** On M1/ARM hardware, certain x86 Docker images required QEMU binfmt emulation to run. This constraint was configured once and carried forward throughout the program.

### Key Concepts

- Containers vs. virtual machines: isolation model and resource sharing
- Docker image, container, and layer architecture
- `docker-compose.yml` structure: services, images, ports, networks, volumes
- Declarative infrastructure as code
- ARM/x86 compatibility via QEMU binfmt emulation

### Artifact

`docker-compose.yml` — initial multi-container environment definition

### References

NetworkChuck. (2021, April 2). *Docker tutorial for beginners* [Video]. YouTube. https://www.youtube.com/watch?v=42iQKuQodW4

TechWorld with Nana. (2020, November 17). *Docker crash course* [Video]. YouTube. https://www.youtube.com/watch?v=_TlK0-5EJ-Y

---

## Session 11 — Secure Container Configuration

### Summary

Session 11 moved from deploying containers to hardening them. A Dockerfile was written from scratch, and security best practices were applied at the image build level: selecting a minimal base image to reduce attack surface, explicitly declaring only the ports the application requires, avoiding running processes as root by creating and switching to a non-privileged user, and removing unnecessary packages that could serve as pivot points for an attacker who gains container access.

The session made explicit that a container is not inherently secure by default — a misconfigured container running as root with world-accessible ports is an attack vector, not a sandbox. The hardened Dockerfile produced in this session reflected the principle that security must be designed in at the lowest level of the stack, not bolted on afterward.

### Key Concepts

- Dockerfile instruction set: `FROM`, `RUN`, `COPY`, `EXPOSE`, `USER`, `CMD`
- Minimal base images to reduce attack surface
- Non-root user execution inside containers
- Explicit port declaration vs. `--publish-all`
- Layer caching and image size optimization

### Artifact

Dockerfile (secured) — hardened container image definition applying least-privilege principles

### References

Docker. (2023). *Dockerfile best practices*. Docker Documentation. https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

TechWorld with Nana. (2020, November 17). *Docker crash course* [Video]. YouTube. https://www.youtube.com/watch?v=_TlK0-5EJ-Y

---

## Session 12 — "The Conductor & the Fleet": Docker Compose Deployment

### Summary

Session 12 ("The Conductor & the Fleet") brought the week's concepts together in a full orchestrated deployment. A complete multi-container environment was defined and launched using Docker Compose — multiple services communicating across defined internal networks, each container fulfilling a distinct role in the stack. The session demonstrated how Compose manages the startup order, network attachment, and inter-service communication that would otherwise require manual coordination across multiple `docker run` commands.

The deployed stack was treated as a live environment: services were inspected with `docker ps` and `docker logs`, inter-container connectivity was tested, and the environment was torn down cleanly using `docker compose down`. This teardown-and-rebuild cycle reinforced the disposable infrastructure principle: environments that can be destroyed and recreated in seconds have a fundamentally different security posture than environments that are manually configured and never touched again.

### Key Concepts

- Docker Compose orchestration: `docker compose up`, `down`, `ps`, `logs`
- Inter-service networking via Compose-defined networks
- Service dependency and startup order
- Container lifecycle: build → run → inspect → teardown
- Disposable infrastructure as a security principle

### Artifact

`docker-compose.yml` (The Conductor & the Fleet) — complete multi-service orchestration file

### References

Docker. (2023). *Docker Compose overview*. Docker Documentation. https://docs.docker.com/compose/

NetworkChuck. (2021, April 2). *Docker tutorial for beginners* [Video]. YouTube. https://www.youtube.com/watch?v=42iQKuQodW4

---

## TLAB-04 — "Operation Hyper-Stack"

### Summary

TLAB-04 ("Operation Hyper-Stack") was the week's independent take-home lab, requiring the deployment of a multi-container stack defined entirely in `docker-compose.yml` and the production of a structured audit of the running environment. The stack was brought up, inspected, and the configuration state of each service — ports, networks, environment variables, image source — was documented and exported as a JSON audit report (`hyperstack_audit.json`). A sandbox report (`sandbox_report.txt`) confirmed the environment provisioned correctly, and `deploy_web.sh` provided a shell script automating the deployment sequence.

The lab reinforced the audit mindset: knowing what is running in your environment, what it is connected to, and what it is exposing is not optional configuration management — it is the baseline visibility required for any security posture.

### Key Concepts

- Full stack deployment and post-deployment audit
- JSON as a structured format for configuration documentation
- Automated deployment via shell script
- Environment verification and baseline documentation

### Artifacts

`hyperstack_audit.json` · `sandbox_report.txt` · `deploy_web.sh`

### References

Docker. (2023). *Docker Compose overview*. Docker Documentation. https://docs.docker.com/compose/

NetworkChuck. (2021, April 2). *Docker tutorial for beginners* [Video]. YouTube. https://www.youtube.com/watch?v=42iQKuQodW4

---

*AaX3 · TKH IFCS Phase One · Week 04 · 2026*