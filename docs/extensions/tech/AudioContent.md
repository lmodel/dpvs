---
search:
  boost: 10.0
---

# Class: AudioContent 


_Content that is or has an audio component_



<div data-search-exclude markdown="1">



URI: [tech:AudioContent](https://w3id.org/lmodel/dpv/tech/AudioContent)





```mermaid
 classDiagram
    class AudioContent
    click AudioContent href "../AudioContent/"
      Content <|-- AudioContent
        click Content href "../Content/"
      
      
```





## Inheritance
* [Content](Content.md) [ [InputOutput](InputOutput.md)]
    * **AudioContent**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:AudioContent](https://w3id.org/lmodel/dpv/tech/AudioContent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Audio Content




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#AudioContent |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:AudioContent |
| native | tech:AudioContent |
| exact | dpv_tech:AudioContent, dpv_tech_owl:AudioContent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AudioContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#AudioContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Content that is or has an audio component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Audio Content
exact_mappings:
- dpv_tech:AudioContent
- dpv_tech_owl:AudioContent
is_a: Content
class_uri: tech:AudioContent

```
</details>

### Induced

<details>
```yaml
name: AudioContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#AudioContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Content that is or has an audio component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Audio Content
exact_mappings:
- dpv_tech:AudioContent
- dpv_tech_owl:AudioContent
is_a: Content
class_uri: tech:AudioContent

```
</details></div>