
/* =====================================
   ARLETTE TORRES - PORTFOLIO
   JavaScript Functionality
===================================== */

// About Me content
const aboutContent = document.getElementById("about-content");

aboutContent.innerHTML = `
    <p>
        I am a Computer Science student at Lamar University,
        working toward my bachelor's degree with an expected
        graduation date of December 2026. I also hold an
        Associate's degree in Biological Sciences from
        Lamar Institute of Technology.
    </p>

    <br>

    <p>
        My technical interests include cybersecurity,
        information technology, software development,
        network security, and digital forensics. Through
        my academic coursework and independent projects,
        I have gained experience with programming languages
        such as Java, C++, C, and Python, as well as Linux,
        Ubuntu, MySQL, and development tools.
    </p>

    <br>

    <p>
        My professional interests are focused on cybersecurity
        operations, particularly Security Operations Center
        (SOC) analysis and incident response. I am interested
        in understanding security alerts, identifying
        suspicious activity, investigating potential threats,
        and learning how organizations protect their systems
        and networks.
    </p>

    <br>

    <p>
        I have also gained professional experience through
        an internship with NUGASYS, where I had exposure to
        digital forensics and technology-related discussions.
        These experiences have strengthened my interest in
        applying technical knowledge to real-world challenges.
    </p>

    <br>

    <p>
        My goal is to begin my career in an entry-level
        cybersecurity or IT position, continue developing
        my technical skills, and pursue professional
        certifications. I am committed to continuous learning
        and building practical experience that will help me
        grow into a cybersecurity professional.
    </p>
`;

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
        const target = document.querySelector(this.getAttribute("href"));

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
