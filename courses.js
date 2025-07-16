console.log("courses.js loaded");
const courses = [
  {
    subject: "CSE",
    number: 110,
    title: "Introduction to Programming",
    credits: 2,
    certificate: "Web and Computer Programming",
    description:
      "This course will introduce students to programming. It will introduce the building blocks of programming languages (variables, decisions, calculations, loops, array, and input/output) and use them to solve problems.",
    technology: ["Python"],
    completed: false,
  },
  {
    subject: "WDD",
    number: 130,
    title: "Web Fundamentals",
    credits: 2,
    certificate: "Web and Computer Programming",
    description:
      "This course introduces students to the World Wide Web and to careers in web site design and development. The course is hands on with students actually participating in simple web designs and programming. It is anticipated that students who complete this course will understand the fields of web design and development and will have a good idea if they want to pursue this degree as a major.",
    technology: ["HTML", "CSS"],
    completed: false,
  },
  {
    subject: "CSE",
    number: 111,
    title: "Programming with Functions",
    credits: 2,
    certificate: "Web and Computer Programming",
    description:
      "CSE 111 students become more organized, efficient, and powerful computer programmers by learning to research and call functions written by others; to write, call , debug, and test their own functions; and to handle errors within functions. CSE 111 students write programs with functions to solve problems in many disciplines, including business, physical science, human performance, and humanities.",
    technology: ["Python"],
    completed: false,
  },
  {
    subject: "CSE",
    number: 210,
    title: "Programming with Classes",
    credits: 2,
    certificate: "Web and Computer Programming",
    description:
      "This course will introduce the notion of classes and objects. It will present encapsulation at a conceptual level. It will also work with inheritance and polymorphism.",
    technology: ["C#"],
    completed: false,
  },
  {
    subject: "WDD",
    number: 131,
    title: "Dynamic Web Fundamentals",
    credits: 2,
    certificate: "Web and Computer Programming",
    description:
      "This course builds on prior experience in Web Fundamentals and programming. Students will learn to create dynamic websites that use JavaScript to respond to events, update content, and create responsive user experiences.",
    technology: ["HTML", "CSS", "JavaScript"],
    completed: false,
  },
  {
    subject: "WDD",
    number: 231,
    title: "Frontend Web Development I",
    credits: 2,
    certificate: "Web and Computer Programming",
    description:
      "This course builds on prior experience with Dynamic Web Fundamentals and programming. Students will focus on user experience, accessibility, compliance, performance optimization, and basic API usage.",
    technology: ["HTML", "CSS", "JavaScript"],
    completed: false,
  },
];

document.addEventListener("DOMContentLoaded", () => {
  const showAll = document.getElementById("all");
  const showWdd = document.getElementById("wdd");
  const showCse = document.getElementById("cse");
  const courseDetails = document.getElementById("courses-details");
  const credits = document.getElementById("credits");

  // all of our event listeners here
  showAll.addEventListener("click", () => {
    output(courses, "ALL");
  });

  showWdd.addEventListener("click", () => {
    const wddCourses = courses.filter((c) => c.subject.toUpperCase() === "WDD");
    output(wddCourses, "WDD");
  });

  showCse.addEventListener("click", () => {
    const cseCourses = courses.filter((c) => c.subject.toUpperCase() === "CSE");
    output(cseCourses, "CSE");
  });

  // I didn't change this because it works, and is about as easy as we can make it.
  function displayCourseDetails(course) {
    // This is a simple way to make your components because it just sets the
    // innerHTML equal to what you would see usually. The "`" indicate a template
    // literal, which is basically a fancy way of saying string, but you can
    // have line breaks, and the "${}" indicate a variable
    courseDetails.innerHTML = `
            <button id="closeModal">X</button>
            <h2>${course.subject} ${course.number}</h2>
            <h3>${course.title}</h3>
            <p><strong>Credits</strong>: ${course.credits}</p>
            <p>${course.description}</p>
            <p><strong>Technologies</strong>: ${course.technology.join(
              ", "
            )}</p>
        `;
    // this just tells javascript to open it as a modal, or dialog window
    courseDetails.showModal();

    document.getElementById("closeModal").addEventListener("click", () => {
      // close the modal
      courseDetails.close();
    });
  }

  // The tutorial you followed does some clever things like set data-subject and
  // data-credit attributes that they use to find and parse the course credits
  // My problem with this is that you have the data, so manipulate it directly
  // because it is way easier.
  function output(courses, type) {
    // courses is the data, type is the subject "WDD", "CSE", or "ALL"
    const container = document.querySelector(".boxcertificate01");
    let totalCredits = 0;
    const totalCreditsElement = document.getElementById("totalCreditsCert01");

    // this empties the container
    container.replaceChildren();

    // loop through the courses passed in and create the elements.
    courses.forEach((course) => {
      const courseDiv = document.createElement("div");
      courseDiv.classList.add(
        "course",
        course.completed ? "courseComplete" : "courseNoComplete"
      );
      courseDiv.setAttribute("data-subject", course.subject);
      courseDiv.setAttribute("data-credits", course.credits);

      const courseTitle = document.createElement("h3");
      courseTitle.textContent = `${course.subject} ${course.number}`;
      courseDiv.appendChild(courseTitle);

      if (container) {
        container.appendChild(courseDiv);
      }

      courseDiv.addEventListener("click", () => {
        displayCourseDetails(course);
      });
    });
    // call the next function to set the total credits, pass "WDD", "CSE", or "ALL"
    updateCredits(type);
  }

  function updateCredits(filter) {
    let totalCredits = 0;
    let filteredCourseArray = [...courses];

    if (filter !== "ALL") {
      filteredCourseArray = filteredCourseArray.filter(
        (course) => course.subject === filter
      );
    }

    filteredCourseArray.forEach((course) => {
      totalCredits += course.credits;
    });

    credits.innerHTML = totalCredits;

    // The way they did it parses through the DOM and finds the data, but
    // we already have that so I'm using it directly.

    // document.querySelectorAll(".course").forEach((course) => {
    //   const credits = parseInt(course.getAttribute("data-credits"), 10);
    //   const subject = course.getAttribute("data-subject").trim().toUpperCase();

    //   if (filter === "ALL" || filter === subject) {
    //     totalCredits += credits;
    //   }
    // });

    // document.getElementById(
    //   "totalCreditsCert01"
    // ).innerHTML = `<strong>Total Credits:</strong> ${totalCredits}`;
  }

  const boxButtons = document.querySelectorAll(".boxButton button");
  boxButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const filter = button.value.trim().toUpperCase();

      document.querySelectorAll(".course").forEach((course) => {
        const subject = course
          .getAttribute("data-subject")
          .trim()
          .toUpperCase();
        course.style.display =
          filter === "ALL" || filter === subject ? "block" : "none";
      });

      updateCredits(filter);
    });
  });

  // This is basically the same as clicking the all button
  document.querySelector('.course-nav button[value="all"]').click();

  // This is a duplicate. If something breaks comment out the top version
  // and uncomment this one to see which is working.

  // function displayCourseDetails(course) {
  //   courseDetails.innerHTML = `
  //           <button id="closeModal">X</button>
  //           <h2>${course.subject} ${course.number}</h2>
  //           <h3>${course.title}</h3>
  //           <p><strong>Credits</strong>: ${course.credits}</p>
  //           <p>${course.description}</p>
  //           <p><strong>Technologies</strong>: ${course.technology.join(
  //             ", "
  //           )}</p>
  //       `;
  //   courseDetails.showModal();

  //   document.getElementById("closeModal").addEventListener("click", () => {
  //     courseDetails.close();
  //   });
  // }

  output(courses, "ALL");
});
