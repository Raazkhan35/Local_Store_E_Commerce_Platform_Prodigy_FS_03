{% for product in products %}
    <div class="product">
        <img src="{{ product.image.url }}" alt="{{ product.name }}">
        <h3>{{ product.name }}</h3>
        <p>Price: ${{ product.price }}</p>
        <a href="{% url 'product_detail' product.pk %}">View Details</a>
    </div>
{% endfor %}
