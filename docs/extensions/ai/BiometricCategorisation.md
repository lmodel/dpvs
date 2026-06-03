---
search:
  boost: 10.0
---

# Class: BiometricCategorisation 


_Capability involving assigning natural persons to specific categories_

_based on their biometric data_



<div data-search-exclude markdown="1">



URI: [ai:BiometricCategorisation](https://w3id.org/lmodel/dpv/ai/BiometricCategorisation)





```mermaid
 classDiagram
    class BiometricCategorisation
    click BiometricCategorisation href "../BiometricCategorisation/"
      Capability <|-- BiometricCategorisation
        click Capability href "../Capability/"
      BiometricCapability <|-- BiometricCategorisation
        click BiometricCapability href "../BiometricCapability/"
      
      
```





## Inheritance
* [AI](AI.md)
    * [Capability](Capability.md)
        * [HumanOrientedCapability](HumanOrientedCapability.md)
            * [BiometricCapability](BiometricCapability.md) [ [Capability](Capability.md)]
                * **BiometricCategorisation** [ [Capability](Capability.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:BiometricCategorisation](https://w3id.org/lmodel/dpv/ai/BiometricCategorisation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Biometric Categorisation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#BiometricCategorisation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:BiometricCategorisation |
| native | ai:BiometricCategorisation |
| exact | dpv_ai:BiometricCategorisation, dpv_ai_owl:BiometricCategorisation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiometricCategorisation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiometricCategorisation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability involving assigning natural persons to specific categories

  based on their biometric data'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Biometric Categorisation
exact_mappings:
- dpv_ai:BiometricCategorisation
- dpv_ai_owl:BiometricCategorisation
is_a: BiometricCapability
mixins:
- Capability
class_uri: ai:BiometricCategorisation

```
</details>

### Induced

<details>
```yaml
name: BiometricCategorisation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#BiometricCategorisation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Capability involving assigning natural persons to specific categories

  based on their biometric data'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Biometric Categorisation
exact_mappings:
- dpv_ai:BiometricCategorisation
- dpv_ai_owl:BiometricCategorisation
is_a: BiometricCapability
mixins:
- Capability
class_uri: ai:BiometricCategorisation

```
</details></div>