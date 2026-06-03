---
search:
  boost: 10.0
---

# Class: DataAggregation 


_Processing operation where data is aggregated, e.g. by combining_

_multiple records into one_



<div data-search-exclude markdown="1">



URI: [ai:DataAggregation](https://w3id.org/lmodel/dpv/ai/DataAggregation)





```mermaid
 classDiagram
    class DataAggregation
    click DataAggregation href "../DataAggregation/"
      DataPreparation <|-- DataAggregation
        click DataPreparation href "../DataPreparation/"
      
      
```





## Inheritance
* [DataOperation](DataOperation.md)
    * [DataPreparation](DataPreparation.md)
        * **DataAggregation**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DataAggregation](https://w3id.org/lmodel/dpv/ai/DataAggregation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Data Aggregation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#DataAggregation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DataAggregation |
| native | ai:DataAggregation |
| exact | dpv_ai:DataAggregation, dpv_ai_owl:DataAggregation |
| close | iso42001:DataResource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataAggregation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataAggregation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is aggregated, e.g. by combining

  multiple records into one'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Aggregation
exact_mappings:
- dpv_ai:DataAggregation
- dpv_ai_owl:DataAggregation
close_mappings:
- iso42001:DataResource
is_a: DataPreparation
class_uri: ai:DataAggregation

```
</details>

### Induced

<details>
```yaml
name: DataAggregation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DataAggregation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Processing operation where data is aggregated, e.g. by combining

  multiple records into one'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Data Aggregation
exact_mappings:
- dpv_ai:DataAggregation
- dpv_ai_owl:DataAggregation
close_mappings:
- iso42001:DataResource
is_a: DataPreparation
class_uri: ai:DataAggregation

```
</details></div>