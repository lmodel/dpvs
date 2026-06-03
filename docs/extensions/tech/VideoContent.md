---
search:
  boost: 10.0
---

# Class: VideoContent 


_Content that is or has a video component_



<div data-search-exclude markdown="1">



URI: [tech:VideoContent](https://w3id.org/lmodel/dpv/tech/VideoContent)





```mermaid
 classDiagram
    class VideoContent
    click VideoContent href "../VideoContent/"
      Content <|-- VideoContent
        click Content href "../Content/"
      
      
```





## Inheritance
* [Content](Content.md) [ [InputOutput](InputOutput.md)]
    * **VideoContent**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:VideoContent](https://w3id.org/lmodel/dpv/tech/VideoContent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Video Content




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#VideoContent |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:VideoContent |
| native | tech:VideoContent |
| exact | dpv_tech:VideoContent, dpv_tech_owl:VideoContent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VideoContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#VideoContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Content that is or has a video component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Video Content
exact_mappings:
- dpv_tech:VideoContent
- dpv_tech_owl:VideoContent
is_a: Content
class_uri: tech:VideoContent

```
</details>

### Induced

<details>
```yaml
name: VideoContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#VideoContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Content that is or has a video component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Video Content
exact_mappings:
- dpv_tech:VideoContent
- dpv_tech_owl:VideoContent
is_a: Content
class_uri: tech:VideoContent

```
</details></div>