---
search:
  boost: 10.0
---

# Class: ImageContent 


_Content that is or has an image component_



<div data-search-exclude markdown="1">



URI: [tech:ImageContent](https://w3id.org/lmodel/dpv/tech/ImageContent)





```mermaid
 classDiagram
    class ImageContent
    click ImageContent href "../ImageContent/"
      Content <|-- ImageContent
        click Content href "../Content/"
      
      
```





## Inheritance
* [Content](Content.md) [ [InputOutput](InputOutput.md)]
    * **ImageContent**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ImageContent](https://w3id.org/lmodel/dpv/tech/ImageContent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Image Content




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ImageContent |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ImageContent |
| native | tech:ImageContent |
| exact | dpv_tech:ImageContent, dpv_tech_owl:ImageContent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ImageContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ImageContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Content that is or has an image component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Image Content
exact_mappings:
- dpv_tech:ImageContent
- dpv_tech_owl:ImageContent
is_a: Content
class_uri: tech:ImageContent

```
</details>

### Induced

<details>
```yaml
name: ImageContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ImageContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Content that is or has an image component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Image Content
exact_mappings:
- dpv_tech:ImageContent
- dpv_tech_owl:ImageContent
is_a: Content
class_uri: tech:ImageContent

```
</details></div>