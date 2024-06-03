MODEl_PATH = 'weights/plant_disease_classifier.h5'
FRONT_PAGE = """
<body style="font-family: Arial, sans-serif; color: #333; font-size: 16px;">
    <p>Welcome to the "Plant Disease Detection using CNN" Streamlit web application. This tool is designed to assist you in identifying the health status of your plants with the help of a Convolutional Neural Network (CNN). Whether you are a home gardener or a farmer, early detection of plant diseases can make a significant difference in preserving the well-being of your plants and optimizing crop yields.</p>
    <h2>How It Works</h2>
    <ol>
        <li><strong>Upload an Image:</strong> To get started, simply upload an image of your plant. The image should be clear and centered on the plant.</li>
        <li><strong>Prediction:</strong> Once you've uploaded an image, click the "Predict" button. Our pre-trained CNN model will analyze the image to determine whether the plant is "Healthy," affected by "Powdery Mildew," or has signs of "Rust."</li>
        <li><strong>Confidence Score:</strong> The application will provide you with a confidence score, indicating how sure the model is about its prediction.</li>
    </ol>
    <h2>Why Use This App?</h2>
    <ul>
        <li><strong>Early Disease Detection:</strong> Detecting plant diseases early can help prevent the spread of diseases and reduce crop losses.</li>
        <li><strong>Easy to Use:</strong> You don't need to be an expert in plant pathology. This user-friendly tool simplifies the process of disease detection.</li>
        <li><strong>Quick Results:</strong> In just a few seconds, you'll receive a classification result with a confidence score.</li>
    </ul>
    <h2>About</h2>
    <p>This web application is built using Streamlit and powered by a deep learning model. It offers a user-friendly interface for plant disease detection, making it accessible to anyone interested in plant health.</p>
    <h2>Get Started</h2>
    <p>To begin using this application, follow these steps:</p>
    <ol>
        <li>Click the "Upload an Image" button in the sidebar.</li>
        <li>Select an image of your plant from your device.</li>
        <li>Click the "Predict" button to see the classification result.</li>
    </ol>
    <p>Whether you are a professional farmer or a hobbyist gardener, this tool can help you keep your plants healthy and thriving. Try it out and make informed decisions about plant care!</p>
    <h2>Acknowledgments</h2>
    <p>We acknowledge the efforts of the open-source community in developing and sharing the model used in this application. This tool would not be possible without their contributions.</p>
    <p>If you have any feedback or suggestions for improving this application, we welcome your input. Together, we can help plants thrive and promote sustainable agriculture.</p>
    <p>Thank you for using the "Plant Disease Detection using CNN" web app!</p>
</body>
"""

RUST_SOLUTIONS = """
Disease : Puccinia
Conventional Method Solution for Rust in Plants:

1. Fungicides: If rust is creeping into your crops, chemical fungicides can come to the rescue. These specially formulated solutions are like superhero shields against rust pathogens. Apply them as directed on the label, usually requiring multiple rounds during the growing season.

2. Crop Rotation: Give rust the old switcheroo! By rotating your crops, you break the disease's chain, stopping it in its tracks. Mix up what you plant in the affected area each season to throw off those pesky rust fungi.

3. Sanitation: A clean field is a happy field! Keep your planting area tidy by clearing out any infected plant debris or weeds. Dispose of these nasties properly to prevent rust from hitching a ride to healthy plants.

4. Resistant Varieties: Give rust a run for its money by planting varieties that are tough as nails. Look for plants that have been bred to resist rust diseases. They'll stand strong against rust, reducing the need for chemical treatments and protecting your yields.

Natural Method Solution for Rust in Plants:

1. Neem Oil: Time to call in nature's cavalry! Neem oil is a natural warrior against rust fungi. Mix it up according to the instructions and spray it on your plants to send rust packing.

2. Baking Soda Solution: Raid your kitchen for this natural remedy! Mix baking soda with water to create a solution that rust fungi can't stand. Give your plants a good spray to create an inhospitable environment for rust.

3. Milk: Got milk? You're in luck! This kitchen staple doubles as a natural fungicide. Mix it with water and spray it on your plants to keep rust at bay. Repeat every week or so for maximum effect.

4. Copper-Based Fungicides: Mother Nature's copper shield! These organic-approved fungicides disrupt rust fungi, keeping them from spreading. Follow the instructions on the label to apply them safely and effectively.

5. Companion Planting: Rust won't stand a chance against this tag team! Plant garlic, onions, or marigolds alongside your susceptible crops to repel rust fungi. It's like having a natural bodyguard for your plants!


- Conventional Fungicides:
    * [Neem Oil from IFFCO Bazar](https://www.iffcobazar.in/en/product/doctor-neem-organic-pest-repellent)
    * [Copper Based Fungicides from IFFCO Bazar](https://www.iffcobazar.in/en/product/gozaru-copper-oxychloride-50-wp)
    * [Ziram fungicide](https://www.militellofarmsupply.com/shop/ziram-xcel-fungicide/)
    * [Captan fungicide](https://www.amazon.com/captan/s?k=captan)
    * [Tebuconazole fungicide](https://www.amazon.com/Tebuconazole-3-6-Select-Gallon-Compare/dp/B07D83RXQ5)

- Natural Fungicides:
    * [Neem Oil from IFFCO Bazar](https://www.iffcobazar.in/en/product/doctor-neem-organic-pest-repellent)
    * [Baking soda](https://www.amazon.com/baking-soda/s?k=baking+soda)
    * Milk: Milk is a common household item and unlikely to be sold on IFFCO Bazar or Amazon.in


"""

POWDERY_SOLUTIONS = """
Disease : Erysiphe cichoracearum
Conventional Method Solution for Powdery Mildew in Plants:

1. Fungicides: Powdery mildew doesn't stand a chance against chemical fungicides. Apply these specially formulated solutions as directed on the label to protect your plants from the powdery menace.

2. Pruning: Trim away infected plant parts to stop powdery mildew in its tracks. Remove any affected leaves, stems, or branches, and dispose of them properly to prevent the spread of the disease.

3. Air Circulation: Powdery mildew loves still air. Keep the air flowing around your plants by spacing them properly and pruning them to improve airflow. This helps dry out the leaves and creates an environment that's less hospitable to powdery mildew.

4. Water Management: Keep your plants hydrated, but not too hydrated! Water the soil around the base of your plants instead of overhead to keep the leaves dry. This helps prevent powdery mildew spores from germinating and spreading.

Natural Method Solution for Powdery Mildew in Plants:

1. Baking Soda Solution: Raid your kitchen for this natural remedy! Mix baking soda with water to create a solution that powdery mildew can't stand. Give your plants a good spray to create an inhospitable environment for the fungus.

2. Milk: Got milk? You're in luck! This kitchen staple doubles as a natural fungicide. Mix it with water and spray it on your plants to keep powdery mildew at bay. Repeat every week or so for maximum effect.

3. Neem Oil: Time to call in nature's cavalry! Neem oil is a natural warrior against powdery mildew. Mix it up according to the instructions and spray it on your plants to send powdery mildew packing.

4. Companion Planting: Powdery mildew won't stand a chance against this tag team! Plant garlic, onions, or chives alongside your susceptible crops to repel powdery mildew. It's like having a natural bodyguard for your plants!

5. Vinegar Solution: Create a homemade vinegar solution by mixing vinegar with water. Spray this solution on your plants to kill powdery mildew spores on contact. Be sure to test it on a small area first to avoid damaging your plants.

## Powdery Mildew Solutions

### Conventional Method Solution

* Fungicides:  While not found on IFFCO Bazar, here's an option on Amazon.in (Note: Always prioritize authorized retailers for fungicides due to regulations): [https://www.amazon.com/captan/s?k=captan](https://www.amazon.com/captan/s?k=captan)
* Pruning Shears:  Here are some on Amazon.in: Pruning Shears on Amazon.in: [https://www.amazon.in/Gardening-Scissors-50-Off-or-more/s?rh=n%3A3639024031%2Cp_n_pct-off-with-tax%3A2665401031](https://www.amazon.in/Gardening-Scissors-50-Off-or-more/s?rh=n%3A3639024031%2Cp_n_pct-off-with-tax%3A2665401031)
* Air Circulation: Improve air flow around plants by proper spacing and pruning.
* Water Management: Water the soil directly, not overhead, to keep leaves dry. 

### Natural Method Solution

* Baking Soda Solution: Mix baking soda with water and spray on plants. (See Amazon.in for baking soda: [https://www.amazon.in/baking-soda/s?k=baking+soda](https://www.amazon.in/baking-soda/s?k=baking+soda))
* Milk: Mix milk with water and spray on plants. Milk is a common household item.
* Neem Oil:  A natural fungicide. Neem Oil from IFFCO Bazar: [https://www.iffcobazar.in/en/product/doctor-neem-organic-pest-repellent](https://www.iffcobazar.in/en/product/doctor-neem-organic-pest-repellent)
* Companion Planting: Plant garlic, onions, or chives near susceptible crops.
* Vinegar Solution: Mix vinegar with water and test on a small area before spraying on plants. Vinegar is a common household item.



"""

HEALTHY_SOLUTIONS = """
Tips for Keeping Crops Healthy:

1. Crop Rotation: Rotate your crops each growing season to prevent the buildup of pests and diseases in the soil. This practice helps break pest and disease cycles and promotes soil health.

2. Soil Management: Maintain healthy soil by practicing good soil management techniques such as regular soil testing, proper fertilization, and adding organic matter like compost or cover crops. Healthy soil supports robust crop growth and reduces the risk of nutrient deficiencies and soil-borne diseases.

3. Integrated Pest Management (IPM): Implement IPM strategies to manage pests and diseases in your crops. This approach combines cultural, biological, and chemical control methods to minimize pest damage while minimizing the use of synthetic pesticides.

4. Weed Control: Keep weeds under control to prevent competition for resources like water, nutrients, and sunlight. Use mulches, cover crops, mechanical cultivation, and targeted herbicides to manage weed populations and maintain crop health.

5. Proper Irrigation: Ensure crops receive adequate and uniform irrigation to support healthy growth and development. Use irrigation methods like drip irrigation or soaker hoses to deliver water directly to the root zone and minimize water waste.

6. Timely Harvesting: Harvest crops at the right time to maximize yield and quality. Monitor crop maturity and harvest when fruits or vegetables are ripe to avoid overripening or spoilage. Prompt harvesting also prevents pest and disease damage during storage.

7. Disease Prevention: Take preventive measures to minimize the risk of crop diseases. Practice crop spacing to improve airflow and reduce humidity around plants, use disease-resistant varieties whenever possible, and avoid overhead irrigation to minimize leaf wetness.

8. Nutrient Management: Monitor soil fertility levels and provide crops with balanced nutrition through proper fertilization. Adjust fertilizer applications based on soil test results and crop nutrient requirements to avoid nutrient imbalances and deficiencies.

9. Environmental Stewardship: Practice sustainable farming methods that promote environmental stewardship and conservation of natural resources. Implement conservation practices such as crop rotation, cover cropping, and reduced tillage to improve soil health and minimize erosion.

10. Continuous Learning: Stay informed about the latest research, technologies, and best practices in crop production. Attend workshops, conferences, and extension events, and consult with agricultural experts to improve your farming knowledge and skills.
"""
