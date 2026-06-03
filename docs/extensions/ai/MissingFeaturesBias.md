---
search:
  boost: 10.0
---

# Class: MissingFeaturesBias 


_Bias that occurs when features are missing from individual training_

_samples_



<div data-search-exclude markdown="1">



URI: [ai:MissingFeaturesBias](https://w3id.org/lmodel/dpv/ai/MissingFeaturesBias)





```mermaid
 classDiagram
    class MissingFeaturesBias
    click MissingFeaturesBias href "../MissingFeaturesBias/"
      RiskConcept <|-- MissingFeaturesBias
        click RiskConcept href "../RiskConcept/"
      DataBias <|-- MissingFeaturesBias
        click DataBias href "../DataBias/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [AIBias](AIBias.md)
        * [DataBias](DataBias.md) [ [RiskConcept](RiskConcept.md)]
            * **MissingFeaturesBias** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:MissingFeaturesBias](https://w3id.org/lmodel/dpv/ai/MissingFeaturesBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Missing Features Bias


## Comments

* If the frequency of missing features is higher for one group than
another then this presents another vector for bias



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/ai/owl#MissingFeaturesBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:MissingFeaturesBias |
| native | ai:MissingFeaturesBias |
| exact | dpv_ai:MissingFeaturesBias, dpv_ai_owl:MissingFeaturesBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MissingFeaturesBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#MissingFeaturesBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs when features are missing from individual training

  samples'
comments:
- 'If the frequency of missing features is higher for one group than

  another then this presents another vector for bias'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Missing Features Bias
exact_mappings:
- dpv_ai:MissingFeaturesBias
- dpv_ai_owl:MissingFeaturesBias
is_a: DataBias
mixins:
- RiskConcept
class_uri: ai:MissingFeaturesBias

```
</details>

### Induced

<details>
```yaml
name: MissingFeaturesBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#MissingFeaturesBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs when features are missing from individual training

  samples'
comments:
- 'If the frequency of missing features is higher for one group than

  another then this presents another vector for bias'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Missing Features Bias
exact_mappings:
- dpv_ai:MissingFeaturesBias
- dpv_ai_owl:MissingFeaturesBias
is_a: DataBias
mixins:
- RiskConcept
class_uri: ai:MissingFeaturesBias

```
</details></div>