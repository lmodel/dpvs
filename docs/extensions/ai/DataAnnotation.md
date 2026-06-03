---
search:
  boost: 10.0
---

# Class: DataAnnotation 


_Processing operation where data is annoated, e.g. by adding additional_

_metadata or context to make it useful_



<div data-search-exclude markdown="1">



URI: [ai:DataAnnotation](https://w3id.org/lmodel/dpv/ai/DataAnnotation)





```mermaid
 classDiagram
    class DataAnnotation
    click DataAnnotation href "../DataAnnotation/"
      DataPreparation <|-- DataAnnotation
        click DataPreparation href "../DataPreparation/"
      

      DataAnnotation <|-- DataLabelling
        click DataLabelling href "../DataLabelling/"
      

      
```





## Inheritance
* [DataOperation](DataOperation.md)
    * [DataPreparation](DataPreparation.md)
        * **DataAnnotation**
            * [DataLabelling](DataLabelling.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataAnnotation](https://w3id.org/lmodel/dpv/ai/DataAnnotation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Annotation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataAnnotation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataAnnotation |
| native | ai:DataAnnotation |
| exact | dpv_ai:DataAnnotation, dpv_ai_owl:DataAnnotation |
| close | iso42001:DataResource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataAnnotation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataAnnotation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is annoated, e.g. by adding additional

  metadata or context to make it useful'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Annotation
exact_mappings:
- dpv_ai:DataAnnotation
- dpv_ai_owl:DataAnnotation
close_mappings:
- iso42001:DataResource
is_a: DataPreparation
class_uri: ai:DataAnnotation

```
</details>

### Induced

<details>
```yaml
name: DataAnnotation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataAnnotation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is annoated, e.g. by adding additional

  metadata or context to make it useful'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Annotation
exact_mappings:
- dpv_ai:DataAnnotation
- dpv_ai_owl:DataAnnotation
close_mappings:
- iso42001:DataResource
is_a: DataPreparation
class_uri: ai:DataAnnotation

```
</details></div>