---
search:
  boost: 10.0
---

# Class: DataLabelling 


_Processing operation where data annotation is carried out through_

_labelling, e.g. by assigning tags or categories_



<div data-search-exclude markdown="1">



URI: [ai:DataLabelling](https://w3id.org/lmodel/dpv/ai/DataLabelling)





```mermaid
 classDiagram
    class DataLabelling
    click DataLabelling href "../DataLabelling/"
      DataAnnotation <|-- DataLabelling
        click DataAnnotation href "../DataAnnotation/"
      
      
```





## Inheritance
* [DataOperation](DataOperation.md)
    * [DataPreparation](DataPreparation.md)
        * [DataAnnotation](DataAnnotation.md)
            * **DataLabelling**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataLabelling](https://w3id.org/lmodel/dpv/ai/DataLabelling) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Labelling




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataLabelling |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataLabelling |
| native | ai:DataLabelling |
| exact | dpv_ai:DataLabelling, dpv_ai_owl:DataLabelling |
| close | iso42001:DataResource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataLabelling
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataLabelling
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data annotation is carried out through

  labelling, e.g. by assigning tags or categories'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Labelling
exact_mappings:
- dpv_ai:DataLabelling
- dpv_ai_owl:DataLabelling
close_mappings:
- iso42001:DataResource
is_a: DataAnnotation
class_uri: ai:DataLabelling

```
</details>

### Induced

<details>
```yaml
name: DataLabelling
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataLabelling
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data annotation is carried out through

  labelling, e.g. by assigning tags or categories'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Labelling
exact_mappings:
- dpv_ai:DataLabelling
- dpv_ai_owl:DataLabelling
close_mappings:
- iso42001:DataResource
is_a: DataAnnotation
class_uri: ai:DataLabelling

```
</details></div>