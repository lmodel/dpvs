---
search:
  boost: 10.0
---

# Class: DataPreparation 


_Processing operation where data is prepared, e.g. organising and_

_transforming it to make it ready for use_



<div data-search-exclude markdown="1">



URI: [ai:DataPreparation](https://w3id.org/lmodel/dpv/ai/DataPreparation)





```mermaid
 classDiagram
    class DataPreparation
    click DataPreparation href "../DataPreparation/"
      DataOperation <|-- DataPreparation
        click DataOperation href "../DataOperation/"
      

      DataPreparation <|-- DataAggregation
        click DataAggregation href "../DataAggregation/"
      DataPreparation <|-- DataAnnotation
        click DataAnnotation href "../DataAnnotation/"
      DataPreparation <|-- DataCleaning
        click DataCleaning href "../DataCleaning/"
      DataPreparation <|-- DataEnrichment
        click DataEnrichment href "../DataEnrichment/"
      DataPreparation <|-- DataUpdating
        click DataUpdating href "../DataUpdating/"
      

      
```





## Inheritance
* [DataOperation](DataOperation.md)
    * **DataPreparation**
        * [DataAggregation](DataAggregation.md)
        * [DataAnnotation](DataAnnotation.md)
        * [DataCleaning](DataCleaning.md)
        * [DataEnrichment](DataEnrichment.md)
        * [DataUpdating](DataUpdating.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataPreparation](https://w3id.org/lmodel/dpv/ai/DataPreparation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Preparation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataPreparation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataPreparation |
| native | ai:DataPreparation |
| exact | dpv_ai:DataPreparation, dpv_ai_owl:DataPreparation |
| close | iso42001:DataResource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataPreparation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataPreparation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is prepared, e.g. organising and

  transforming it to make it ready for use'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Preparation
exact_mappings:
- dpv_ai:DataPreparation
- dpv_ai_owl:DataPreparation
close_mappings:
- iso42001:DataResource
is_a: DataOperation
class_uri: ai:DataPreparation

```
</details>

### Induced

<details>
```yaml
name: DataPreparation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataPreparation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is prepared, e.g. organising and

  transforming it to make it ready for use'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Preparation
exact_mappings:
- dpv_ai:DataPreparation
- dpv_ai_owl:DataPreparation
close_mappings:
- iso42001:DataResource
is_a: DataOperation
class_uri: ai:DataPreparation

```
</details></div>