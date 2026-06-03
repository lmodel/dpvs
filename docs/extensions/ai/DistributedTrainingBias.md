---
search:
  boost: 10.0
---

# Class: DistributedTrainingBias 


_Bias that occurs due to distributed machine having different sources of_

_data that do not have the same distribution of feature space_



<div data-search-exclude markdown="1">



URI: [ai:DistributedTrainingBias](https://w3id.org/lmodel/dpv/ai/DistributedTrainingBias)





```mermaid
 classDiagram
    class DistributedTrainingBias
    click DistributedTrainingBias href "../DistributedTrainingBias/"
      RiskConcept <|-- DistributedTrainingBias
        click RiskConcept href "../RiskConcept/"
      DataBias <|-- DistributedTrainingBias
        click DataBias href "../DataBias/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [AIBias](AIBias.md)
        * [DataBias](DataBias.md) [ [RiskConcept](RiskConcept.md)]
            * **DistributedTrainingBias** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DistributedTrainingBias](https://w3id.org/lmodel/dpv/ai/DistributedTrainingBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Distributed Training Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DistributedTrainingBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DistributedTrainingBias |
| native | ai:DistributedTrainingBias |
| exact | dpv_ai:DistributedTrainingBias, dpv_ai_owl:DistributedTrainingBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DistributedTrainingBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DistributedTrainingBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to distributed machine having different sources
  of

  data that do not have the same distribution of feature space'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Distributed Training Bias
exact_mappings:
- dpv_ai:DistributedTrainingBias
- dpv_ai_owl:DistributedTrainingBias
is_a: DataBias
mixins:
- RiskConcept
class_uri: ai:DistributedTrainingBias

```
</details>

### Induced

<details>
```yaml
name: DistributedTrainingBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DistributedTrainingBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to distributed machine having different sources
  of

  data that do not have the same distribution of feature space'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Distributed Training Bias
exact_mappings:
- dpv_ai:DistributedTrainingBias
- dpv_ai_owl:DistributedTrainingBias
is_a: DataBias
mixins:
- RiskConcept
class_uri: ai:DistributedTrainingBias

```
</details></div>