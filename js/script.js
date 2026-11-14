
/* =====================================
   ARLETTE TORRES - PORTFOLIO
   JavaScript Functionality
===================================== */

// About Me content
const aboutContent = document.getElementById("about-content");

if (aboutContent) {
    aboutContent.innerHTML = `
        <p>
            I am a Computer Science student at Lamar University,
            working toward my bachelor's degree with an expected
            graduation date of December 2026. I also hold an
            Associate's degree in Biological Sciences from
            Lamar Institute of Technology. My academic background
            has helped me develop analytical thinking,
            problem-solving, and technical skills that I continue
            applying to my coursework and independent projects.
        </p>

        <br>

        <p>
            My technical interests include cybersecurity,
            information technology, software development,
            network security, and digital forensics. Through
            my academic coursework and independent projects,
            I have gained experience with programming languages
            such as Java, C++, C, and Python, as well as Linux,
            Ubuntu, MySQL, and various development tools.
        </p>

        <br>

        <p>
            My professional interests are focused on cybersecurity
            operations, particularly Security Operations Center
            (SOC) analysis and incident response. I am interested
            in understanding security alerts, identifying
            suspicious activity, investigating potential threats,
            and learning how organizations protect their systems
            and networks. I am especially interested in developing
            practical skills in threat detection and security
            monitoring.
        </p>

        <br>

        <p>
            I have also gained professional experience through
            an internship with NUGASYS, where I had exposure to
            digital forensics and technology-related discussions.
            These experiences strengthened my interest in applying
            technical knowledge to real-world challenges and
            learning more about investigative technologies.
        </p>

        <br>

        <p>
            Through my university projects, I have developed
            experience working with databases, networking concepts,
            software development, and collaborative programming.
            I have worked with tools such as Git, GitHub, VirtualBox,
            MySQL, and Node.js while completing assignments and
            team-based projects. These experiences have helped me
            strengthen my problem-solving abilities, troubleshoot
            technical issues, and understand the importance of
            organized code, documentation, and communication
            throughout the software development process.
        </p>

        <br>

        <p>
            My goal is to begin my career in an entry-level
            cybersecurity or IT position, particularly as a SOC
            Analyst, while continuing to develop my technical
            knowledge and practical experience. I plan to pursue
            professional certifications, strengthen my understanding
            of security tools, and continue building projects that
            demonstrate my abilities. I am committed to continuous
            learning and developing the skills necessary to grow
            into a cybersecurity professional.
        </p>
    `;
}

// Update footer year automatically
const footer = document.querySelector("footer");

if (footer) {
    footer.innerHTML = `
        <p>&copy; ${new Date().getFullYear()}
        Arlette Torres. All rights reserved.</p>
    `;
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener("click", function(event) {
        const target = document.querySelector(
            this.getAttribute("href")
        );

        if (target) {
            event.preventDefault();

            target.scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});

// Console message for development
console.log("Arlette Torres portfolio loaded successfully!");
