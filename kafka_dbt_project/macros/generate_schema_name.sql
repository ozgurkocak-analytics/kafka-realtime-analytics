{% macro generate_schema_name(custom_schema_name, node) %}
    {% if target.name == 'dev' %}
        {{ target.schema }}
    {% else %}
        {{ custom_schema_name }}
    {% endif %}
{% endmacro %}