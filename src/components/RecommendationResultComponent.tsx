import React, { useMemo } from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  ReferenceDot,
} from 'recharts';

export interface CO2LifecycleDataPoint {
  stage: string;
  standardCO2: number;
  recommendedCO2: number;
  reductionPct?: number;
}

export interface RecommendationResultComponentProps {
  foodName?: string;
  standardMaterial?: string;
  recommendedMaterial?: string;
  baselineCO2Total?: number;
  recommendedCO2Total?: number;
  reductionPercentage?: number;
  data?: CO2LifecycleDataPoint[];
  className?: string;
}

const DEFAULT_LIFECYCLE_DATA: CO2LifecycleDataPoint[] = [
  { stage: 'Resin Raw', standardCO2: 120, recommendedCO2: 74, reductionPct: 38 },
  { stage: 'Film Extrusion', standardCO2: 95, recommendedCO2: 60, reductionPct: 37 },
  { stage: 'Highway Transit', standardCO2: 65, recommendedCO2: 48, reductionPct: 26 },
  { stage: 'Retail Shelf', standardCO2: 45, recommendedCO2: 28, reductionPct: 38 },
  { stage: 'End-of-Life', standardCO2: 85, recommendedCO2: 30, reductionPct: 65 },
];

export const RecommendationResultComponent: React.FC<RecommendationResultComponentProps> = ({
  foodName = 'Commodity Produce',
  standardMaterial = 'Standard Virgin Polyolefin (LDPE / Monolayer)',
  recommendedMaterial = 'Optimized Barrier / Down-Gauged Recycled Polymer',
  baselineCO2Total = 410,
  recommendedCO2Total = 240,
  reductionPercentage = 41,
  data = DEFAULT_LIFECYCLE_DATA,
  className = '',
}) => {
  const chartData = useMemo(() => {
    return data.map((d) => ({
      ...d,
      savedCO2: Math.max(0, d.standardCO2 - d.recommendedCO2),
      reductionPct:
        d.reductionPct ??
        (d.standardCO2 > 0
          ? Math.round(((d.standardCO2 - d.recommendedCO2) / d.standardCO2) * 100)
          : 0),
    }));
  }, [data]);

  const totalStandard = useMemo(
    () => chartData.reduce((acc, curr) => acc + curr.standardCO2, 0) || baselineCO2Total,
    [chartData, baselineCO2Total]
  );

  const totalRecommended = useMemo(
    () => chartData.reduce((acc, curr) => acc + curr.recommendedCO2, 0) || recommendedCO2Total,
    [chartData, recommendedCO2Total]
  );

  const netSavings = Math.max(0, totalStandard - totalRecommended);
  const netSavingsPct = totalStandard > 0 ? Math.round((netSavings / totalStandard) * 100) : reductionPercentage;

  return (
    <div
      className={`recharts-co2-card ${className}`}
      style={{
        background: '#ffffff',
        border: '1.5px solid #d1fae5',
        borderRadius: '12px',
        padding: '1.25rem',
        boxShadow: '0 4px 14px rgba(16, 185, 129, 0.08)',
        fontFamily: 'inherit',
        marginTop: '1.25rem',
        marginBottom: '1.25rem',
      }}
    >
      {/* Header with Title and Reduction Pill */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '0.75rem',
          marginBottom: '0.75rem',
        }}
      >
        <div>
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.4rem',
              fontSize: '0.72rem',
              fontWeight: 800,
              letterSpacing: '0.05em',
              textTransform: 'uppercase',
              color: '#059669',
              background: '#ecfdf5',
              padding: '0.2rem 0.55rem',
              borderRadius: '999px',
              marginBottom: '0.35rem',
            }}
          >
            <span>🌱</span> PROJECTED CO₂ FOOTPRINT REDUCTION
          </div>
          <h4
            style={{
              fontSize: '1.05rem',
              fontWeight: 800,
              color: '#0f172a',
              margin: 0,
              lineHeight: 1.3,
            }}
          >
            Lifecycle Emissions: Standard vs Recommended Material
          </h4>
        </div>

        <div
          style={{
            display: 'flex',
            alignItems: 'baseline',
            gap: '0.4rem',
            background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)',
            color: '#ffffff',
            padding: '0.4rem 0.85rem',
            borderRadius: '8px',
            boxShadow: '0 2px 6px rgba(16, 185, 129, 0.25)',
          }}
        >
          <span style={{ fontSize: '1.25rem', fontWeight: 900 }}>-{netSavingsPct}%</span>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, opacity: 0.9 }}>CO₂e Net Cut</span>
        </div>
      </div>

      {/* Material Comparison Subheader */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          fontSize: '0.785rem',
          color: '#64748b',
          marginBottom: '1rem',
          paddingBottom: '0.75rem',
          borderBottom: '1px dashed #e2e8f0',
          flexWrap: 'wrap',
          gap: '0.5rem',
        }}
      >
        <div>
          <span style={{ color: '#94a3b8', fontWeight: 600 }}>Standard Baseline: </span>
          <strong style={{ color: '#475569' }}>{standardMaterial}</strong>
        </div>
        <div>
          <span style={{ color: '#059669', fontWeight: 600 }}>Recommended Solution: </span>
          <strong style={{ color: '#047857' }}>{recommendedMaterial}</strong>
        </div>
      </div>

      {/* Small Recharts Line Chart */}
      <div style={{ width: '100%', height: 210 }}>
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            data={chartData}
            margin={{ top: 12, right: 16, left: -18, bottom: 4 }}
          >
            <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" vertical={false} />
            <XAxis
              dataKey="stage"
              tick={{ fontSize: 11, fill: '#64748b', fontWeight: 600 }}
              stroke="#cbd5e1"
              tickLine={false}
            />
            <YAxis
              tick={{ fontSize: 10, fill: '#94a3b8' }}
              stroke="#cbd5e1"
              tickLine={false}
              unit="kg"
            />
            <Tooltip
              content={({ active, payload, label }) => {
                if (active && payload && payload.length) {
                  const std = payload.find((p) => p.dataKey === 'standardCO2')?.value as number;
                  const rec = payload.find((p) => p.dataKey === 'recommendedCO2')?.value as number;
                  const saved = Math.max(0, (std ?? 0) - (rec ?? 0));
                  const pct = std ? Math.round((saved / std) * 100) : 0;
                  return (
                    <div
                      style={{
                        background: '#0f172a',
                        color: '#ffffff',
                        padding: '0.65rem 0.85rem',
                        borderRadius: '8px',
                        fontSize: '0.785rem',
                        boxShadow: '0 8px 20px rgba(0,0,0,0.25)',
                        lineHeight: 1.5,
                      }}
                    >
                      <div style={{ fontWeight: 800, color: '#38bdf8', marginBottom: '0.3rem' }}>
                        Lifecycle Stage: {label}
                      </div>
                      <div style={{ color: '#cbd5e1' }}>
                        Standard Baseline: <strong>{std} kg CO₂e</strong>
                      </div>
                      <div style={{ color: '#4ade80' }}>
                        PackSense Material: <strong>{rec} kg CO₂e</strong>
                      </div>
                      <div
                        style={{
                          marginTop: '0.3rem',
                          paddingTop: '0.3rem',
                          borderTop: '1px solid rgba(255,255,255,0.15)',
                          color: '#facc15',
                          fontWeight: 700,
                        }}
                      >
                        Projected Saving: -{saved} kg CO₂e (-{pct}%)
                      </div>
                    </div>
                  );
                }
                return null;
              }}
            />
            <Legend
              wrapperStyle={{ fontSize: '11px', paddingTop: '6px' }}
              iconType="circle"
              iconSize={8}
            />
            <Line
              type="monotone"
              dataKey="standardCO2"
              name="Standard Packaging (kg CO₂e)"
              stroke="#94a3b8"
              strokeWidth={2}
              strokeDasharray="4 4"
              dot={{ r: 3, fill: '#94a3b8' }}
              activeDot={{ r: 5 }}
            />
            <Line
              type="monotone"
              dataKey="recommendedCO2"
              name="Recommended Material (kg CO₂e)"
              stroke="#10b981"
              strokeWidth={2.5}
              dot={{ r: 4, fill: '#10b981', strokeWidth: 1.5, stroke: '#ffffff' }}
              activeDot={{ r: 6, fill: '#059669' }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Bottom Summary Metric Row */}
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))',
          gap: '0.65rem',
          marginTop: '0.85rem',
          paddingTop: '0.75rem',
          borderTop: '1px solid #f1f5f9',
          fontSize: '0.8rem',
        }}
      >
        <div style={{ background: '#f8fafc', padding: '0.5rem 0.75rem', borderRadius: '6px' }}>
          <span style={{ color: '#64748b', fontSize: '0.72rem', display: 'block' }}>Standard Footprint</span>
          <strong style={{ color: '#334155', fontSize: '0.95rem' }}>{totalStandard} kg CO₂e</strong>
        </div>
        <div style={{ background: '#ecfdf5', padding: '0.5rem 0.75rem', borderRadius: '6px' }}>
          <span style={{ color: '#047857', fontSize: '0.72rem', display: 'block' }}>Recommended Footprint</span>
          <strong style={{ color: '#059669', fontSize: '0.95rem' }}>{totalRecommended} kg CO₂e</strong>
        </div>
        <div style={{ background: '#f0fdf4', padding: '0.5rem 0.75rem', borderRadius: '6px' }}>
          <span style={{ color: '#15803d', fontSize: '0.72rem', display: 'block' }}>Net CO₂ Avoided</span>
          <strong style={{ color: '#166534', fontSize: '0.95rem' }}>-{netSavings} kg (-{netSavingsPct}%)</strong>
        </div>
      </div>
    </div>
  );
};

export default RecommendationResultComponent;
