const locations = [
    { title: "1 THE PYLON", coords: "1117,599,1061,544", shape: "rect", image: "images/pylon.jpg", description: "The Pylon originally stood for the true, the good, and the beautiful." },
    { title: "2 THE MURAL", coords: "982,568,1044,623", shape: "rect", image: "images/mural.jpg", description: "The sculpture was built by national artist Eduardo Castrillo in 1974." },
    { title: "3 VISITOR'S LOUNGE", coords: "1058,557,1010,510", shape: "rect", image: "images/visitors-lounge.jpg", description: "A place for guests and visitors to rest." },
    { title: "4 OPEN COURT", coords: "1121,540,1061,485", shape: "rect", image: "images/open-court.jpg", description: "An open space for recreational activities." },
    { title: "5 LAWN TENNIS COURT", coords: "972,446,1027,499", shape: "rect", image: "images/tennis-court.jpg", description: "A tennis court for students and faculty." },
    { title: "6 BASKETBALL COURT", coords: "858,393,955,444", shape: "rect", image: "images/basketball-court.jpg", description: "A venue for basketball games and tournaments." },
    { title: "7 SOUVENIR SHOP", coords: "775,449,837,502", shape: "rect", image: "images/souvenir-shop.jpg", description: "A shop selling PUP memorabilia." },
    { title: "8 MABINI SHRINE", coords: "689,413,741,457", shape: "rect", image: "images/mabini-shrine.jpg", description: "A tribute to Apolinario Mabini." },
    { title: "9 MABINI MUSEUM", coords: "625,410,675,456", shape: "rect", image: "images/mabini-museum.jpg", description: "A museum showcasing Mabini's legacy." },
    { title: "10 OBELISK", coords: "774,410,699,344", shape: "rect", image: "images/obelisk.jpg", description: "The Obelisk symbolizes the university's resilience and excellence." },
    { title: "11 FREEDOM PARK", coords: "566,386,622,446", shape: "rect", image: "images/freedom-park.jpg", description: "A park dedicated to student expression." },
    { title: "12 FOUNTAIN PARK", coords: "440,425,537,463", shape: "rect", image: "images/fountain-park.jpg", description: "A relaxing area with a fountain feature." },
    { title: "13 INTER-FAITH CHAPEL", coords: "220,402,373,486", shape: "rect", image: "images/chapel.jpg", description: "A place for worship and reflection." },
    { title: "14 MAIN ACADEMIC BUILDING", coords: "441,372,278,283", shape: "rect", image: "images/main-building.jpg", description: "The Main Academic Building houses several colleges and administrative offices." },
    { title: "15 GAZEBO", coords: "62,358,110,398", shape: "rect", image: "images/PUPLogo.png", description: "A shaded area for relaxation." },
    { title: "16 GRANDSTAND", coords: "554,462,682,507", shape: "rect", image: "images/grandstand.jpg", description: "A seating area for sports events and ceremonies." },
    { title: "17 OVAL", coords: "500,523,634,636", shape: "rect", image: "images/oval1.jpg", description: "An area for running and sports events." },
    { title: "18 TAHANAN NG ATLETA", coords: "499,653,582,722", shape: "rect", image: "images/tahanan-atleta.jpg", description: "A dormitory for student-athletes." },
    { title: "19 GABRIELA SILANG BUILDING", coords: "392,676,475,765", shape: "rect", image: "images/PUPLogo.png", description: "A building named after Gabriela Silang." },
    { title: "20 FOOD AND NUTRITION BUILDING", coords: "87,409,157,492", shape: "rect", image: "images/food-nutrition.jpg", description: "A facility for food and nutrition studies." },
    { title: "21 FACILITY MANAGEMENT OFFICE", coords: "244,243,316,304", shape: "rect", image: "images/facility_management.jpg", description: "The office responsible for campus maintenance and operations." },
    { title: "22 SAMPAGUITA BUILDING", coords: "425,239,457,280", shape: "rect", image: "images/sampaguita_building.jpg", description: "A building named after the national flower, housing various offices." },
    { title: "23 STUDENT CENTER", coords: "492,289,462,243", shape: "rect", image: "images/student_center.jpg", description: "A hub for student activities, organizations, and events." },
    { title: "24 CHARLIE DEL ROSARIO BUILDING", coords: "512,251,579,297", shape: "rect", image: "images/charlie_del_rosario.jpg", description: "An academic building named in honor of Charlie Del Rosario." },
    { title: "25 LINEAR PARK", coords: "534,206,586,248", shape: "rect", image: "images/linear_park.jpg", description: "A relaxing green space for students and faculty." },
    { title: "26 LABORATORY HIGH SCHOOL BUILDING", coords: "592,197,691,248", shape: "rect", image: "images/laboratory_high_school.jpg", description: "A facility for high school students focusing on hands-on learning." },
    { title: "27 PRINTING PRESS BUILDING", coords: "641,166,693,195", shape: "rect", image: "images/printing_press.jpg", description: "The university's official printing and publication center." },
    { title: "28 PROPERTY AND SUPPLY MANAGEMENT OFFICE", coords: "701,209,732,179", shape: "rect", image: "images/property_supply.jpg", description: "Manages procurement, inventory, and distribution of supplies." },
    { title: "29 WATER TOWER", coords: "734,208,762,232", shape: "rect", image: "images/water_tower.jpg", description: "A historic water tower providing campus water supply." },
    { title: "30 NINOY AQUINO LEARNING RESOURCE CENTER", coords: "705,250,824,308", shape: "rect", image: "images/ninoy_aquino_center.jpg", description: "A resource center with a library and digital learning facilities." },
    { title: "31 LAGOON COMMERCIAL SPACES", coords: "558,299,605,325", shape: "rect", image: "images/lagoon_commercial.jpg", description: "Shops and dining options for students and visitors." },
    { title: "32 AMPHITHEATER", coords: "472,302,532,330", shape: "rect", image: "images/amphitheater.jpg", description: "An open-air venue for performances and events." },
    { title: "33 LAGOON PARK", coords: "609,326,692,367", shape: "rect", image: "images/lagoon_park.jpg", description: "A scenic park with a lagoon, ideal for relaxation." },
    { title: "34 NUTRITION & FOOD TECHNOLOGY RESEARCH AND DEVELOPMENT CENTER BUILDING", coords: "897,306,835,242", shape: "rect", image: "images/nutrition_center.jpg", description: "A research hub for food technology and nutrition science." },
    { title: "35 HUMAN KINETICS BUILDING", coords: "818,313,880,369", shape: "rect", image: "images/human_kinetics.jpg", description: "Home to sports and physical education programs." },
    { title: "36 TAHANAN NG ALUMNI", coords: "905,300,959,342", shape: "rect", image: "images/tahanan_alumni.jpg", description: "A meeting place for alumni gatherings and events." },
    { title: "37 SWIMMING POOL", coords: "934,347,996,384", shape: "rect", image: "images/swimming_pool.jpg", description: "A standard-sized pool used for recreation and training." },
    { title: "38 MULTI-PURPOSE BUILDING", coords: "1037,358,1203,427", shape: "rect", image: "images/multi_purpose.jpg", description: "A versatile space for university activities and events." },
    { title: "39 ENGINEERING AND SCIENCE RESEARCH CENTER", coords: "1196,439,1282,518", shape: "rect", image: "images/engineering_science.jpg", description: "A research facility for engineering and science innovations." },
    { title: "40 COMMUNICATION BUILDING", coords: "1014,136,1069,169", shape: "rect", image: "images/communication_building.jpg", description: "Houses the communication and media studies department." },
    { title: "41 PUP THEATER", coords: "1030,103,1068,133", shape: "rect", image: "images/pup_theater.jpg", description: "A venue for cultural performances and theater arts." },
    { title: "42 ENGINEERING AND ARCHITECTURE BUILDING", coords: "1080,96,1122,130", shape: "rect", image: "images/engineering_architecture.jpg", description: "Home to engineering and architecture courses." },
    { title: "43 CONDOTEL", coords: "936,40,996,85", shape: "rect", image: "images/condotel.jpg", description: "Accommodation facility for visitors and university guests." },
    { title: "44 NDC TENNIS COURT AND CLUB HOUSE", coords: "1140,116,1182,145", shape: "rect", image: "images/ndc_tennis.jpg", description: "A sports facility featuring tennis courts and a clubhouse." },
    { title: "45 NDC COVERED COURT", coords: "1131,85,1184,109", shape: "rect", image: "images/ndc_covered_court.jpg", description: "A covered court for indoor sports and events." },
    { title: "46 BUSINESS PROCESSING OFFICE", coords: "1214,90,1248,116", shape: "rect", image: "images/PUPLogo.png", description: "Handles business transactions and financial services." },
    { title: "47 INFORMATION TECHNOLOGY BUILDING", coords: "1202,42,1255,85", shape: "rect", image: "images/it_building.jpg", description: "Houses IT and computer science programs." },
    { title: "48 ANTIQUE HOUSE", coords: "1127,51,1173,82", shape: "rect", image: "images/antique_house.jpg", description: "A historical house showcasing antique collections." },
    { title: "49 GRADUATE SCHOOL", coords: "1297,6,1339,42", shape: "rect", image: "images/graduate_school.jpg", description: "Dedicated to postgraduate studies and research." },
    { title: "50 HASMIN BUILDING", coords: "1374,7,1426,68", shape: "rect", image: "images/hasmin_building.jpg", description: "A multi-purpose academic building." },
    { title: "15 GAZEBO", coords: "512,506,414,483", shape: "rect", image: "images/gazebo1.jpg", description: "A shaded area for relaxation." }
];

function openModal(title, imageSrc, description, event) {
    const modal = document.getElementById("modal");
    if (!modal) return;

    document.getElementById("modal-title").innerText = title;
    document.getElementById("modal-image").src = imageSrc;
    document.getElementById("modal-description").innerText = description;

    modal.style.visibility = "hidden";
    modal.style.display = "block";

    let mouseX = event.clientX;
    let mouseY = event.clientY;

    const modalWidth = modal.offsetWidth;
    const modalHeight = modal.offsetHeight;
    const windowWidth = document.documentElement.clientWidth; 
    const windowHeight = document.documentElement.clientHeight;
    const offset = 15;

    let finalX = mouseX + offset;
    let finalY = mouseY + offset;

    if (finalX + modalWidth > windowWidth) {
        finalX = windowWidth - modalWidth - offset;
    }

    if (finalY + modalHeight > windowHeight) {
        finalY = windowHeight - modalHeight - offset;
    }

    if (finalX < 0) {
        finalX = offset;
    }

    if (finalY < 0) {
        finalY = offset;
    }

    modal.style.left = `${finalX}px`;
    modal.style.top = `${finalY}px`;
    modal.style.visibility = "visible";
}

function closeModal() {
    const modal = document.getElementById("modal");
    if (modal) {
        modal.style.display = "none";
    }
}


function generateMapAreas() {
    const map = document.getElementById("pup-map");

    if (!map) return;

    locations.forEach((location) => {
        const area = document.createElement("area");
        area.shape = location.shape;
        area.coords = location.coords;
        area.href = "#";
        area.alt = location.title;
        area.title = location.title;

        area.addEventListener("mouseenter", (event) => openModal(location.title, location.image, location.description, event));
        area.addEventListener("mouseleave", closeModal);

        map.appendChild(area);
    });

    if (typeof imageMapResize === "function") {
        imageMapResize();
    }
}

window.addEventListener("load", generateMapAreas);
