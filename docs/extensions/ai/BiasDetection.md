---
search:
  boost: 10.0
---

# Class: BiasDetection 


_Indicates measures to detect bias_



<div data-search-exclude markdown="1">



URI: [ai:BiasDetection](https://w3id.org/lmodel/dpv/ai/BiasDetection)





```mermaid
 classDiagram
    class BiasDetection
    click BiasDetection href "../BiasDetection/"
      BiasAssessment <|-- BiasDetection
        click BiasAssessment href "../BiasAssessment/"
      
      
```





## Inheritance
* [BiasAssessment](BiasAssessment.md)
    * **BiasDetection**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BiasDetection](https://w3id.org/lmodel/dpv/ai/BiasDetection) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Bias Detection




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BiasDetection |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BiasDetection |
| native | ai:BiasDetection |
| exact | dpv_ai:BiasDetection, dpv_ai_owl:BiasDetection |
| close | iso42001:AISystemImpactAssessment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiasDetection
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiasDetection
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates measures to detect bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bias Detection
exact_mappings:
- dpv_ai:BiasDetection
- dpv_ai_owl:BiasDetection
close_mappings:
- iso42001:AISystemImpactAssessment
is_a: BiasAssessment
class_uri: ai:BiasDetection

```
</details>

### Induced

<details>
```yaml
name: BiasDetection
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiasDetection
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Indicates measures to detect bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Bias Detection
exact_mappings:
- dpv_ai:BiasDetection
- dpv_ai_owl:BiasDetection
close_mappings:
- iso42001:AISystemImpactAssessment
is_a: BiasAssessment
class_uri: ai:BiasDetection

```
</details></div>