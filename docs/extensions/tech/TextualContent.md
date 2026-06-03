---
search:
  boost: 10.0
---

# Class: TextualContent 


_Content that is or has a textual component_



<div data-search-exclude markdown="1">



URI: [tech:TextualContent](https://w3id.org/lmodel/dpv/tech/TextualContent)





```mermaid
 classDiagram
    class TextualContent
    click TextualContent href "../TextualContent/"
      Content <|-- TextualContent
        click Content href "../Content/"
      
      
```





## Inheritance
* [Content](Content.md) [ [InputOutput](InputOutput.md)]
    * **TextualContent**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:TextualContent](https://w3id.org/lmodel/dpv/tech/TextualContent) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Textual Content




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#TextualContent |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:TextualContent |
| native | tech:TextualContent |
| exact | dpv_tech:TextualContent, dpv_tech_owl:TextualContent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TextualContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#TextualContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Content that is or has a textual component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Textual Content
exact_mappings:
- dpv_tech:TextualContent
- dpv_tech_owl:TextualContent
is_a: Content
class_uri: tech:TextualContent

```
</details>

### Induced

<details>
```yaml
name: TextualContent
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#TextualContent
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Content that is or has a textual component
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Textual Content
exact_mappings:
- dpv_tech:TextualContent
- dpv_tech_owl:TextualContent
is_a: Content
class_uri: tech:TextualContent

```
</details></div>